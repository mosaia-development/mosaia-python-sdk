"""Wallets collection (Node parity: collections/wallets.ts)."""

from typing import Any, Dict

from ..models.wallet import Wallet
from .base_collection import BaseCollection


class Wallets(BaseCollection[Dict[str, Any], Wallet, Any, Any]):
    def __init__(self, uri: str = ""):
        super().__init__(f"{uri}/billing/wallet", Wallet)
