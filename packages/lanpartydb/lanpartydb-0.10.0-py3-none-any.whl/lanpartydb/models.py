"""
lanpartydb.models
~~~~~~~~~~~~~~~~~

Data models

:Copyright: 2024-2025 Jochen Kupperschmidt
:License: MIT
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Series:
    slug: str
    name: str
    alternative_names: list[str] = field(default_factory=list)
    country_codes: list[str] = field(default_factory=list)


@dataclass(frozen=True, kw_only=True)
class Party:
    slug: str
    title: str
    series_slug: str | None = field(kw_only=True, default=None)
    organizer_entity: str | None = field(kw_only=True, default=None)
    start_on: date
    end_on: date
    seats: int | None = None
    attendees: int | None = None
    online: bool | None = False
    location: Location | None = None
    links: Links | None = None


@dataclass(frozen=True)
class Location:
    name: str | None = field(kw_only=True, default=None)
    country_code: str
    city: str
    postal_code: str | None = None
    street: str | None = None
    latitude: Decimal | None = None
    longitude: Decimal | None = None


@dataclass(frozen=True)
class Links:
    website: Resource | None


@dataclass(frozen=True)
class Resource:
    url: str
    offline: bool = False
