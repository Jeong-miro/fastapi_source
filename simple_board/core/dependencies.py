from fastapi import Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from utils.security import verify_access_token
from repository.database import get_db
from repository.models.user import User
from exceptions.user import UserNotFoundException,UserCredentialException
from services.user import get_user

# form submit 으로 넘어오는 경우
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")+

# data 만 주고받을 때
security = HTTPBearer()

def get_current_user(credentails:HTTPAuthorizationCredentials=Depends(security),db:Session=Depends(get_db)):
    token = credentails.credentials
    payload = verify_access_token(token)
    user_id= payload.get("sub")

    if user_id is None:
        raise UserCredentialException

    return get_user(db=db, user_id=user_id)
