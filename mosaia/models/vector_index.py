"""Vector index model (Node parity: models/vector-index.ts)."""

from typing import Any, Dict, Optional

from .base import BaseModel


class VectorIndex(BaseModel[Dict[str, Any]]):
    def __init__(self, data: Dict[str, Any], uri: Optional[str] = None):
        super().__init__(data, uri or "/index")

    @property
    def vectors(self):
        from ..collections.vectors import Vectors

        return Vectors(self.get_uri())

    async def reindex_files(self) -> Any:
        response = await self.api_client.post(f"{self.get_uri()}/reindex", {})
        if isinstance(response, dict) and "data" in response:
            return response["data"]
        return response

    async def search(
        self,
        query: str,
        *,
        limit: int = 10,
        params: Optional[Dict[str, Any]] = None,
        exclude: Optional[list] = None,
        embedding_model_id: Optional[str] = None,
        rerank_model_id: Optional[str] = None,
    ) -> Any:
        if not self.data.get("id"):
            raise Exception(
                "VectorIndex must have an id before search; fetch via collection first."
            )
        qp: Dict[str, Any] = {"query": query, "limit": str(limit)}
        if params:
            import json

            qp["params"] = json.dumps(params)
        if exclude:
            import json

            qp["exclude"] = json.dumps(exclude)
        if embedding_model_id:
            qp["embeddingModelId"] = embedding_model_id
        if rerank_model_id:
            qp["rerankModelId"] = rerank_model_id
        response = await self.api_client.get(self.get_uri(), qp)
        if isinstance(response, dict):
            return response
        return {"documents": response, "paging": None}
