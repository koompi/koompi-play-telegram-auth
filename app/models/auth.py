from pydantic import BaseModel


class SignIn(BaseModel):
    phone: str
    force_sms: bool = False


class SignInResponse(BaseModel):
    phone: str
    phone_code_hash: str


class Confirm(SignInResponse):
    code: int


class ConfirmResponse(BaseModel):
    id: str
    phone: str
    # gender: str
    profile: str = None
