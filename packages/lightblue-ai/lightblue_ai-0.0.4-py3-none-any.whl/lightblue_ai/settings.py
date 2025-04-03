from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    default_model: str
    sub_agent_model: str | None = None

    tavily_api_key: str | None = None
    bfl_api_key: str | None = None
    urlbox_api_key: str | None = None
    pixabay_api_key: str | None = None

    mcp_config_path: str = (Path.cwd() / "./mcp.json").expanduser().resolve().absolute().as_posix()

    model_config = SettingsConfigDict(case_sensitive=False, frozen=True, env_file=".env")
