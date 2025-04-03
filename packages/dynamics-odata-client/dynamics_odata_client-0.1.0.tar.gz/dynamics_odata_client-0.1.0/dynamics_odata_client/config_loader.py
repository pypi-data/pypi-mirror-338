from dotenv import load_dotenv
import os
from .config import DynamicsConfig

load_dotenv()

def load_config_from_env() -> DynamicsConfig:
    return DynamicsConfig(
        base_url=os.getenv("DYNAMICS_BASE_URL"),
        auth_url=os.getenv("DYNAMICS_AUTH_URL"),
        auth_data={
            "grant_type": "client_credentials",
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET"),
            "resource": os.getenv("DYNAMICS_BASE_URL")
        },
        retries=int(os.getenv("RETRIES", 3)),
        delay=int(os.getenv("DELAY", 5)),
        timeout=int(os.getenv("TIMEOUT", 15)),
        batch_size=int(os.getenv("BATCH_SIZE", 100))
    )