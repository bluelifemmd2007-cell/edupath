from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import create_token, get_current_user, hash_password, verify_password
from app.database import StudentProfile, User, get_db
from app.schemas import AuthResponse, LoginRequest, RegisterRequest, UserOut

router = APIRouter(prefix="/api/auth", tags=["auth"])


def _user_out(user: User) -> UserOut:
    grade = user.profile.grade if user.profile else None
    return UserOut(
        id=user.id,
        username=user.username,
        email=user.email,
        role=user.role,
        grade=grade,
        created_at=user.created_at,
    )


@router.post("/register", response_model=AuthResponse, status_code=201)
def register(body: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter((User.username == body.username) | (User.email == body.email)).first():
        raise HTTPException(status.HTTP_409_CONFLICT, "نام کاربری یا ایمیل قبلاً ثبت شده")

    user = User(
        username=body.username,
        email=body.email,
        password_hash=hash_password(body.password),
        role="student",
    )
    db.add(user)
    db.flush()

    profile = StudentProfile(user_id=user.id, grade=body.grade)
    db.add(profile)
    db.commit()
    db.refresh(user)

    return AuthResponse(token=create_token(user), user=_user_out(user))


@router.post("/login", response_model=AuthResponse)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        (User.username == body.username) | (User.email == body.username)
    ).first()
    if not user or not verify_password(body.password, user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "نام کاربری یا رمز عبور اشتباه است")

    return AuthResponse(token=create_token(user), user=_user_out(user))


@router.get("/me", response_model=UserOut)
def me(user: User = Depends(get_current_user)):
    return _user_out(user)
