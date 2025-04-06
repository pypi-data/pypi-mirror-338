# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "JSONType",
    "UUIDLike",
    "uuidlike_as_uuid",
)

import typing
from uuid import UUID


JSONType = typing.Any

UUIDLike = UUID | str


def uuidlike_as_uuid(id: UUIDLike) -> UUID:
    if isinstance(id, UUID):
        return id
    if isinstance(id, str):
        return UUID(id)
    raise ValueError(
        f"Invalid UUIDLike value of type {type(id)}, expected 'uuid.UUID' or 'str'"
    )
