from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class Authorization(BaseModel):
    token: str
    user_id: str
    roles: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    permissions: Optional[List[str]] = None
    scopes: Optional[List[str]] = None
    expiration: Optional[datetime] = None
    

class Meta(BaseModel):
    authorization: Optional[Authorization] = None
    timestamp: datetime
    correlation_id: str


class HttpMeta(Meta):
    ip: str


class AsyncMeta(Meta):
    topic: str
    subtopic: Optional[str] = None
    produced_at: Optional[datetime] = None
    consumed_at: Optional[datetime] = None
    retry_count: int = 0
