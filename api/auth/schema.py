from pydantic import BaseModel, Field

class UserList(BaseModel):
    email: str = Field(..., example="test@gmail.com")
    fullname: str = Field(..., example="Test")

class UserCreate(UserList):
    password: str = Field(..., example="test")

class ForgotPassword(BaseModel):
    email: str

class EmailRequest(BaseModel):
    email: str

class PasswordToken(BaseModel):
    password_token: str

class ResetPassword(BaseModel):
    password_token: str
    new_password: str
    confirm_password: str