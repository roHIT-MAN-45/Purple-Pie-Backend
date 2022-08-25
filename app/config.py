from pydantic import BaseSettings

# Setting enviroment variables
class Settings(BaseSettings):
    db_hostname : str
    db_username : str
    db_password : str
    db_port : str
    db_name : str
    secret_key : str
    algorithm : str
    token_expiration_time : int

    class Config:
        env_file = ".env"

settings = Settings()