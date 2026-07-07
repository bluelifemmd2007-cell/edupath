from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6)
    grade: str = "یازدهم"


class LoginRequest(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str
    role: str
    grade: str | None = None
    created_at: datetime | None = None

    model_config = {"from_attributes": True}


class AuthResponse(BaseModel):
    token: str
    user: UserOut


class AssessmentAnswer(BaseModel):
    question_id: str
    value: int = Field(ge=1, le=10)


class AssessmentSubmitRequest(BaseModel):
    answers: list[AssessmentAnswer]


class RecommendationOut(BaseModel):
    key: str
    title: str
    description: str
    match_percent: int


class AssessmentOut(BaseModel):
    id: int
    results: list[RecommendationOut]
    created_at: datetime

    model_config = {"from_attributes": True}


class QuestionOut(BaseModel):
    id: str
    text: str
    category: str
