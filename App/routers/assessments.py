import json

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import Assessment, User, get_db
from app.schemas import AssessmentOut, AssessmentSubmitRequest, QuestionOut, RecommendationOut
from app.services.recommendation import QUESTIONS, recommend_majors

router = APIRouter(prefix="/api/assessments", tags=["assessments"])


@router.get("/questions", response_model=list[QuestionOut])
def get_questions():
    return [QuestionOut(**q) for q in QUESTIONS]


@router.post("/submit", response_model=AssessmentOut, status_code=201)
def submit_assessment(
    body: AssessmentSubmitRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if len(body.answers) < len(QUESTIONS):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "لطفاً به همه سوالات پاسخ دهید")

    answers = {a.question_id: a.value for a in body.answers}
    results = recommend_majors(answers)

    assessment = Assessment(
        student_id=user.id,
        answers=json.dumps(answers, ensure_ascii=False),
        results=json.dumps(results, ensure_ascii=False),
    )
    db.add(assessment)
    db.commit()
    db.refresh(assessment)

    return AssessmentOut(
        id=assessment.id,
        results=[RecommendationOut(**r) for r in results],
        created_at=assessment.created_at,
    )


@router.get("/latest", response_model=AssessmentOut | None)
def get_latest(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    assessment = (
        db.query(Assessment)
        .filter(Assessment.student_id == user.id)
        .order_by(Assessment.created_at.desc())
        .first()
    )
    if not assessment:
        return None

    return AssessmentOut(
        id=assessment.id,
        results=[RecommendationOut(**r) for r in assessment.results_dict],
        created_at=assessment.created_at,
    )


@router.get("/{assessment_id}", response_model=AssessmentOut)
def get_assessment(
    assessment_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    assessment = db.get(Assessment, assessment_id)
    if not assessment or assessment.student_id != user.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "آزمون یافت نشد")

    return AssessmentOut(
        id=assessment.id,
        results=[RecommendationOut(**r) for r in assessment.results_dict],
        created_at=assessment.created_at,
    )
