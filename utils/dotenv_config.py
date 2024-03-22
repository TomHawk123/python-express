import os
from pathlib import Path
from dotenv import load_dotenv


def dotenv_config():
    ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

    # Load .env file based on ENVIRONMENT
    if ENVIRONMENT in ["production", "test"]:
        load_dotenv()
    else:
        env_path = Path('../.env')
        env_path2 = Path('./.env')

        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
        elif env_path2.exists():
            load_dotenv(dotenv_path=env_path2)
        else:
            raise FileNotFoundError(f"""Error: Environment file '{
                                    env_path}' not found!""")


if __name__ == "__main__":
    dotenv_config()
