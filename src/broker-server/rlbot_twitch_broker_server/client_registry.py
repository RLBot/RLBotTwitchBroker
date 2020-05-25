from dataclasses import dataclass
from typing import Dict

@dataclass
class ClientData:
    base_url: str

class ClientRegistry:

    def __init__(self):
        self.clients: Dict[str, ClientData] = {}

    def register_client(self, base_url, client: ClientData):
        self.clients[base_url] = client


CLIENT_REGISTRY: ClientRegistry = None
