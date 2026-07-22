from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)


def create_organization(
    db: Session,
    organization: OrganizationCreate,
):
    db_organization = Organization(**organization.model_dump())

    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)

    return db_organization


def get_organizations(db: Session):
    return (
        db.query(Organization)
        .order_by(Organization.id)
        .all()
    )


def get_organization_by_id(
    db: Session,
    organization_id: int,
):
    return (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )


def get_organization_by_code(
    db: Session,
    organization_code: str,
):
    return (
        db.query(Organization)
        .filter(
            Organization.organization_code == organization_code
        )
        .first()
    )


def get_organization_by_email(
    db: Session,
    email: str,
):
    return (
        db.query(Organization)
        .filter(
            Organization.email == email
        )
        .first()
    )


def update_organization(
    db: Session,
    organization_id: int,
    organization: OrganizationUpdate,
):
    db_organization = get_organization_by_id(
        db,
        organization_id,
    )

    if not db_organization:
        return None

    update_data = organization.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_organization, key, value)

    db.commit()
    db.refresh(db_organization)

    return db_organization


def delete_organization(
    db: Session,
    organization_id: int,
):
    db_organization = get_organization_by_id(
        db,
        organization_id,
    )

    if not db_organization:
        return False

    db.delete(db_organization)
    db.commit()

    return True