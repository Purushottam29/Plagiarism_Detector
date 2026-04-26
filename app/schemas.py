from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ReportHistoryItem(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    file_name: str
    plagiarism_percentage: float
    pdf_path: str
    created_at: datetime
