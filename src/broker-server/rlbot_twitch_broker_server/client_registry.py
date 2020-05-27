from dataclasses import dataclass
from typing import Dict

@dataclass
class ActionServerData:
    base_url: str

    def get_key(self):
        return self.base_url


class ActionServerRegistry:

    def __init__(self):
        self.clients: Dict[str, ActionServerData] = {}

    def register_client(self, client: ActionServerData):
        self.clients[client.get_key()] = client


CLIENT_REGISTRY: ActionServerRegistry = None
