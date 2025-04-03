import time
import requests
import pandas as pd
from typing import Optional
from .config import DynamicsConfig
from .config_loader import load_config_from_env
import logging

logger = logging.getLogger(__name__)

class DynamicsClient:
    def __init__(self, config: DynamicsConfig = None):
        self.config = config or load_config_from_env()
        self._token: Optional[str] = None

    def _refresh_token(self):
        try:
            response = requests.post(self.config.auth_url, data=self.config.auth_data)
            response.raise_for_status()
            token = response.json().get("access_token")
            self._token = f"Bearer {token}"
            logger.info("🔐 Token obtenido correctamente.")
        except requests.RequestException as e:
            logger.error("❌ Error al obtener token: %s", e)
            self._token = None

    def _get_token(self):
        if not self._token:
            self._refresh_token()
        return self._token

    def get_data(self, endpoint: str, query: str = "") -> pd.DataFrame:
        token = self._get_token()
        if not token:
            raise RuntimeError("Token no disponible.")

        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        base_url = f"{self.config.base_url.rstrip('/')}/data/{endpoint.lstrip('/')}"
        final_url = f"{base_url}?{query.lstrip('?')}&$top={self.config.batch_size}&$format=json"

        data = []
        skip = 0
        retries = 0

        while True:
            try:
                paged_url = f"{final_url}&$skip={skip}"
                resp = requests.get(paged_url, headers=headers, timeout=self.config.timeout)

                if resp.status_code == 401 and retries < self.config.retries:
                    logger.warning("🔄 Token expirado. Renovando...")
                    self._refresh_token()
                    retries += 1
                    continue

                resp.raise_for_status()
                chunk = resp.json().get("value", [])
                data.extend(chunk)

                logger.info(f"🔹 Página: {len(chunk)} registros (acumulado: {len(data)})")

                if len(chunk) < self.config.batch_size:
                    break
                skip += self.config.batch_size

            except requests.RequestException as e:
                retries += 1
                logger.warning(f"⚠️ Error en la petición (intento {retries}): {e}")
                if retries >= self.config.retries:
                    logger.error("🚫 Se alcanzó el número máximo de reintentos.")
                    break
                time.sleep(self.config.delay)

        df = pd.DataFrame(data)
        if '@odata.etag' in df.columns:
            df.drop(columns=['@odata.etag'], inplace=True)
        return df