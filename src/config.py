from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    LOCAL_DATABASE_URL:str 
    
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )

Config = Settings()