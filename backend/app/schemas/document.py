from pydantic import BaseModel
from datetime import datetime


class DocumentBase(BaseModel):
    content: str


class ClaudeDocCreate(DocumentBase):
    pass


class InitialDocCreate(DocumentBase):
    pass


class PRPDocCreate(DocumentBase):
    generated_from: str | None = None


class DocumentUpdate(BaseModel):
    content: str


class DocumentInDBBase(DocumentBase):
    id: int
    project_id: int
    version: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ClaudeDoc(DocumentInDBBase):
    pass


class InitialDoc(DocumentInDBBase):
    pass


class PRPDoc(DocumentInDBBase):
    generated_from: str | None