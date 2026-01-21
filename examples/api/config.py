import dotenv, logging, typing
from pydantic import Field, field_validator, ValidationInfo
try:
    from pydantic import BaseSettings
except:
    from pydantic_settings import BaseSettings

class ApiConfig(BaseSettings):
    api_host: str = Field('127.0.0.1')
    api_port: int = Field(5000)
    worker_num: int = Field(1)
    forwarded_allow_ips: str = Field('127.0.0.1')
    model_path: str = Field(...)
    gemma_path: str = Field(...)
    spatial_upsampler_path: typing.Optional[str] = Field(None)

    class Config:
        env_file = dotenv.find_dotenv(usecwd=True)
        env_file_encoding = 'utf-8'
        extra = 'ignore'


config = ApiConfig()


LOGGER = logging.getLogger('gunicorn.error')
LOGGER_ACCESS = logging.getLogger('gunicorn.access')