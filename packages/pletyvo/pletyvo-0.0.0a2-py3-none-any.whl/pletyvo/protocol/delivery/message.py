# Copyright (c) 2024-2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Message",
    "MessageCreateInput",
    "MessageUpdateInput",
)

import typing
from uuid import UUID

import attrs

from pletyvo.protocol import dapp

if typing.TYPE_CHECKING:
    from pletyvo.types import (
        UUIDLike,
    )

message_content_validator = (
    attrs.validators.min_len(1),
    attrs.validators.max_len(2048),
)  # type: ignore[var-annotated]


@attrs.define
class Message:
    body: dapp.EventBody = attrs.field(converter=lambda d: dapp.EventBody.from_str(d))

    auth: dapp.AuthHeader = attrs.field(converter=lambda d: dapp.AuthHeader.from_dict(d))

    @classmethod
    def from_dict(cls, d: dict[str, typing.Any]) -> Message:
        return cls(
            body=d["body"],
            auth=d["auth"],
        )


@attrs.define
class MessageCreateInput:
    channel: UUIDLike = attrs.field(converter=UUID)

    content: str = attrs.field(validator=message_content_validator)


@attrs.define
class MessageUpdateInput:
    message: UUIDLike = attrs.field(converter=UUID)

    channel: UUIDLike = attrs.field(converter=UUID)

    content: str = attrs.field(validator=message_content_validator)
