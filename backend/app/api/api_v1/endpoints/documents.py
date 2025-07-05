from typing import List, Literal
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import get_db
from app.models.document import ClaudeDoc, InitialDoc, PRPDoc
from app.schemas.document import (
    ClaudeDoc as ClaudeDocSchema,
    ClaudeDocCreate,
    InitialDoc as InitialDocSchema,
    InitialDocCreate,
    PRPDoc as PRPDocSchema,
    PRPDocCreate,
    DocumentUpdate
)

router = APIRouter()


@router.post("/claude/{project_id}", response_model=ClaudeDocSchema, status_code=status.HTTP_201_CREATED)
async def create_claude_doc(
    project_id: int,
    doc_in: ClaudeDocCreate,
    db: AsyncSession = Depends(get_db)
) -> ClaudeDoc:
    db_doc = ClaudeDoc(**doc_in.model_dump(), project_id=project_id)
    db.add(db_doc)
    await db.commit()
    await db.refresh(db_doc)
    return db_doc


@router.post("/initial/{project_id}", response_model=InitialDocSchema, status_code=status.HTTP_201_CREATED)
async def create_initial_doc(
    project_id: int,
    doc_in: InitialDocCreate,
    db: AsyncSession = Depends(get_db)
) -> InitialDoc:
    db_doc = InitialDoc(**doc_in.model_dump(), project_id=project_id)
    db.add(db_doc)
    await db.commit()
    await db.refresh(db_doc)
    return db_doc


@router.post("/prp/{project_id}", response_model=PRPDocSchema, status_code=status.HTTP_201_CREATED)
async def create_prp_doc(
    project_id: int,
    doc_in: PRPDocCreate,
    db: AsyncSession = Depends(get_db)
) -> PRPDoc:
    db_doc = PRPDoc(**doc_in.model_dump(), project_id=project_id)
    db.add(db_doc)
    await db.commit()
    await db.refresh(db_doc)
    return db_doc


@router.get("/{doc_type}/{project_id}/latest")
async def get_latest_document(
    doc_type: Literal["claude", "initial", "prp"],
    project_id: int,
    db: AsyncSession = Depends(get_db)
):
    model_map = {
        "claude": ClaudeDoc,
        "initial": InitialDoc,
        "prp": PRPDoc
    }
    
    model = model_map[doc_type]
    result = await db.execute(
        select(model)
        .where(model.project_id == project_id)
        .order_by(model.version.desc())
        .limit(1)
    )
    doc = result.scalar_one_or_none()
    
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{doc_type} document not found for this project"
        )
    
    return doc


@router.put("/{doc_type}/{doc_id}", response_model=dict)
async def update_document(
    doc_type: Literal["claude", "initial", "prp"],
    doc_id: int,
    doc_in: DocumentUpdate,
    db: AsyncSession = Depends(get_db)
):
    model_map = {
        "claude": ClaudeDoc,
        "initial": InitialDoc,
        "prp": PRPDoc
    }
    
    model = model_map[doc_type]
    result = await db.execute(select(model).where(model.id == doc_id))
    doc = result.scalar_one_or_none()
    
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{doc_type} document not found"
        )
    
    # Crear nueva versión
    new_doc = model(
        project_id=doc.project_id,
        content=doc_in.content,
        version=doc.version + 1
    )
    if hasattr(doc, 'generated_from'):
        new_doc.generated_from = doc.generated_from
    
    db.add(new_doc)
    await db.commit()
    await db.refresh(new_doc)
    
    return {"message": "Document updated", "new_version": new_doc.version}