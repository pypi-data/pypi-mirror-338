from forged.__exceptions__ import ConfiguredException
import os
from dotenv import dotenv_values
from typing import Protocol, Optional
from typing import Type, TypeVar, Callable
class SecretProvider(Protocol):
    def get(self, key: str) -> Optional[str]:
        """Return the secret value for the given key, or None if not found."""


class EnvSecretProvider:
    def get(self, key: str) -> Optional[str]:
        return os.getenv(key)


class DotenvSecretProvider:
    def __init__(self, path: str = ".env"):
        self._secrets = dotenv_values(path)

    def get(self, key: str) -> Optional[str]:
        return self._secrets.get(key)

class VaultSecretProvider:
    def __init__(self, client, base_path="myapp/secrets"):
        self.client = client
        self.base_path = base_path

    def get(self, key: str) -> Optional[str]:
        path = f"{self.base_path}/{key}"
        try:
            secret = self.client.secrets.kv.read_secret_version(path=path)
            return secret.get("data", {}).get("data", {}).get(key)
        except Exception as e:
            # TODO: Log the error
            return None


class SecretsManager:
    def __init__(self, *providers: SecretProvider) -> None:
        self.providers = providers
        self._cache = {}

    def get(self, key: str, default: Optional[str] = None, aliases: list[str] = []) -> Optional[str]:
        keys = [key] + aliases
        for k in keys:
            if k in self._cache:
                return self._cache[k]
            for provider in self.providers:
                value = provider.get(k)
                if value is not None:
                    self._cache[k] = value
                    return value
        return default

    def require(self, key: str) -> str:
        val = self.get(key)
        if val is None:
            raise KeyError(f"Secret '{key}' not found in any provider.")
        return val

    def invalidate(self, key: Optional[str] = None) -> None:
        if key:
            self._cache.pop(key, None)
        else:
            self._cache.clear()

    def has(self, key: str) -> bool:
        return self.get(key) is not None


if __name__ == '__main__':
    pass
