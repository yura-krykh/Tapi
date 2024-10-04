from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 29528585
    API_HASH: str = '50ff3a7e7dee2799ca61382e2436b0c5'

    MIN_AVAILABLE_ENERGY: int = 8000
    SLEEP_BY_MIN_ENERGY: list[int] = [1000, 5000]

    ADD_TAPS_ON_TURBO: int = 800

    AUTO_UPGRADE_TAP: bool = False
    MAX_TAP_LEVEL: int = 20
    AUTO_UPGRADE_ENERGY: bool = False
    MAX_ENERGY_LEVEL: int = 20
    AUTO_UPGRADE_CHARGE: bool = False
    MAX_CHARGE_LEVEL: int = 5

    AUTO_UPGRADE_TOWN: bool = False
    MAX_TOWN_LEVEL: int = 20

    APPLY_DAILY_ENERGY: bool = True
    APPLY_DAILY_TURBO: bool = True

    RANDOM_TAPS_COUNT: list[int] = [100, 900]
    SLEEP_BETWEEN_TAP: list[int] = [20, 300]

    USE_PROXY_FROM_FILE: bool = True


settings = Settings()