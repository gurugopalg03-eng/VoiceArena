from sqlalchemy.orm import Session

from app.crud.organization import (
    create_organization,
    delete_organization,
    get_organization_by_id,
    get_organizations,
    update_organization,
)
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)


def create_new_organization(
    db: Session,
    organization: OrganizationCreate,
):
    return create_organization(db, organization)


def get_all_organizations(db: Session):
    return get_organizations(db)


def get_organization(
    db: Session,
    organization_id: int,
):
    return get_organization_by_id(
        db,
        organization_id,
    )


def update_existing_organization(
    db: Session,
    organization_id: int,
    organization: OrganizationUpdate,
):
    return update_organization(
        db,
        organization_id,
        organization,
    )


def delete_existing_organization(
    db: Session,
    organization_id: int,
):
    return delete_organization(
        db,
        organization_id,
    )