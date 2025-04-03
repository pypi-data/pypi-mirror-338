from datetime import datetime
from typing import Self

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship

from mmisp.db.list_json_type import DBListJson
from mmisp.db.mixins import DictMixin
from mmisp.db.mypy import Mapped, mapped_column
from mmisp.db.uuid_type import DBUUID

from ..database import Base


class Organisation(Base, DictMixin):
    __tablename__ = "organisations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    date_created: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    date_modified: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    description: Mapped[str] = mapped_column(Text)
    type: Mapped[str] = mapped_column(String(255))
    nationality: Mapped[str] = mapped_column(String(255))
    sector: Mapped[str] = mapped_column(String(255))
    created_by: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    uuid: Mapped[str] = mapped_column(DBUUID, unique=True)
    contacts: Mapped[str] = mapped_column(Text)
    local: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    restricted_to_domain: Mapped[list[str]] = mapped_column(DBListJson)
    landingpage: Mapped[str] = mapped_column(Text)

    # Relationship to users
    users = relationship("User", back_populates="org", lazy="raise_on_sql")
    creator = relationship(
        "User", primaryjoin="Organisation.created_by == User.id", foreign_keys=created_by, lazy="selectin"
    )
    events = relationship(
        "Event", primaryjoin="Organisation.id == Event.org_id", back_populates="org", lazy="raise_on_sql"
    )  # type:ignore[assignment,var-annotated]
    events_created = relationship(
        "Event", primaryjoin="Organisation.id == Event.orgc_id", back_populates="orgc", lazy="raise_on_sql"
    )  # type:ignore[assignment,var-annotated]

    galaxy_clusters = relationship(
        "GalaxyCluster",
        primaryjoin="Organisation.id == GalaxyCluster.org_id",
        back_populates="org",
        lazy="raise_on_sql",
        foreign_keys="GalaxyCluster.org_id",
    )  # type:ignore[assignment,var-annotated]
    galaxy_clusters_created = relationship(
        "GalaxyCluster",
        primaryjoin="Organisation.id == GalaxyCluster.orgc_id",
        back_populates="orgc",
        lazy="raise_on_sql",
        foreign_keys="GalaxyCluster.orgc_id",
    )  # type:ignore[assignment,var-annotated]

    _sharing_group_orgs = relationship(
        "SharingGroupOrg",
        primaryjoin="Organisation.id == SharingGroupOrg.org_id",
        foreign_keys="SharingGroupOrg.org_id",
        viewonly=True,
        lazy="selectin",
    )

    @property
    def _sharing_group_ids(self: Self) -> list[int]:
        return [x.sharing_group_id for x in self._sharing_group_orgs]


#
