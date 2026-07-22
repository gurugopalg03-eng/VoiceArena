from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse,
    OrganizationUpdate,
)
from app.services.organization_service import (
    create_new_organization,
    delete_existing_organization,
    get_all_organizations,
    get_organization,
    update_existing_organization,
)

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.post(
    "/",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db),
):
    return create_new_organization(db, organization)


@router.get(
    "/",
    response_model=list[OrganizationResponse],
)
def get_organizations(
    db: Session = Depends(get_db),
):
    return get_all_organizations(db)


@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def get_organization_by_id(
    organization_id: int,
    db: Session = Depends(get_db),
):
    organization = get_organization(db, organization_id)

    if not organization:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return organization


@router.put(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def update_organization(
    organization_id: int,
    organization: OrganizationUpdate,
    db: Session = Depends(get_db),
):
    updated = update_existing_organization(
        db,
        organization_id,
        organization,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return updated


@router.delete(
    "/{organization_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_organization(
    organization_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_existing_organization(
        db,
        organization_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return