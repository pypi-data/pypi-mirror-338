from dataclasses import dataclass
from typing import Dict

@dataclass
class DynamicsConfig:
    base_url: str
    auth_url: str
    auth_data: Dict[str, str]
    retries: int
    delay: int
    timeout: int
    batch_size: int