from fastapi import Body, Depends, Request, APIRouter
from starlette.responses import JSONResponse

from providers.config_provider import ConfigProvider
from rest_api.providers.fernet_cryptography_provider import FernetCryptographyProvider
from rest_api.providers.jwt_provider import JWTProvider
from rest_api.models.user_login_schema import UserLoginSchema
from rest_api.models.user import User
from rest_api.providers.user_provider import UserProvider
from rest_api.models.jwt_bearer import JWTBearer

router = APIRouter(prefix="/auth", tags=["auth"])

config_provider = ConfigProvider()
cryptography_provider = FernetCryptographyProvider(config_provider.get_encryption_key())
user_provider = UserProvider(config_provider.get_db_connection_url())
jwt_provider = JWTProvider(
    config_provider.get_jwt_secret(), config_provider.get_jwt_algorithm()
)


@router.get("/whoami", dependencies=[Depends(JWTBearer(jwt_provider))])
async def whoami(request: Request):
    try:
        jb = JWTBearer(jwt_provider)
        tok = await jb(request)
        return jwt_provider.decode_jwt(tok)
    except ValueError:
        JSONResponse({"message": "Incorrect token"})


@router.post("/signup")
async def create_user(user: UserLoginSchema = Body(...)):
    db_user = User(
        email=user.email, password=cryptography_provider.encrypt(user.password)
    )
    user_provider.add_user(db_user)
    return JSONResponse({"message": "User created."})


@router.post("/login")
async def user_login(user: UserLoginSchema = Body(...)):
    if (
        cryptography_provider.decrypt(user_provider.get_user(user.email).password)
        == user.password
    ):
        full_user_info = user_provider.get_user(user.email)
        return JSONResponse(
            {"data": dict(access_token=jwt_provider.sign_jwt(full_user_info))}
        )

    return JSONResponse({"message": "Wrong login details."})
