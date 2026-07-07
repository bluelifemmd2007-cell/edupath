from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.auth import hash_password
from app.database import SessionLocal, User, init_db
from app.routers import assessments, auth

STATIC_DIR = Path(__file__).parent / "static"

app = FastAPI(title="EduPath", version="1.0.0", description="پلتفرم مشاوره تحصیلی")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(auth.router)
app.include_router(assessments.router)


@app.on_event("startup")
def startup():
    init_db()
    db = SessionLocal()
    try:
        if not db.query(User).filter(User.role == "admin").first():
            admin = User(
                username="admin",
                email="admin@edupath.local",
                password_hash=hash_password("admin123"),
                role="admin",
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/assessment")
def assessment_page():
    return FileResponse(STATIC_DIR / "assessment.html")


@app.get("/results")
def results_page():
    return FileResponse(STATIC_DIR / "results.html")


@app.get("/dashboard")
def dashboard_page():
    return FileResponse(STATIC_DIR / "dashboard.html")
