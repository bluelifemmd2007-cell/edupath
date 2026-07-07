import json
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, create_engine, func
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

from app.config import DATABASE_URL


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="student")
    created_at = Column(DateTime, server_default=func.now())

    profile = relationship("StudentProfile", back_populates="user", uselist=False)
    assessments = relationship("Assessment", back_populates="student")


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    grade = Column(String(20), default="یازدهم")
    field = Column(String(50), nullable=True)
    gpa = Column(Float, nullable=True)

    user = relationship("User", back_populates="profile")


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    answers = Column(Text, nullable=False)
    results = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    student = relationship("User", back_populates="assessments")

    @property
    def answers_dict(self) -> dict:
        return json.loads(self.answers)

    @property
    def results_dict(self) -> list:
        return json.loads(self.results)


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def utcnow():
    return datetime.now(timezone.utc)
