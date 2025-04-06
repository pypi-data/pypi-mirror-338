# Copyright (c) 2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = (
    "Post",
    "PostCreateInput",
    "PostUpdateInput",
)

import typing
from uuid import UUID

import attrs

from pletyvo.protocol.dapp import Hash

if typing.TYPE_CHECKING:
    from pletyvo.types import UUIDLike


post_content_validator = (
    attrs.validators.min_len(1),
    attrs.validators.max_len(2048),
)  # type: ignore[var-annotated]


def hash_from_str(s: str) -> Hash:
    return Hash.from_str(s)


@attrs.define
class Post:
    id: UUIDLike = attrs.field(converter=UUID)

    hash: Hash = attrs.field(converter=hash_from_str)

    author: Hash = attrs.field(converter=hash_from_str)

    channel: UUIDLike = attrs.field(converter=UUID)

    content: str = attrs.field(validator=post_content_validator)

    @classmethod
    def from_dict(cls, d: dict[str, typing.Any]) -> Post:
        return cls(
            id=d["id"],
            hash=d["hash"],
            author=d["author"],
            channel=d["channel"],
            content=d["content"],
        )


@attrs.define
class PostCreateInput:
    channel: UUIDLike = attrs.field(converter=UUID)

    content: str = attrs.field(validator=post_content_validator)


@attrs.define
class PostUpdateInput:
    channel: UUIDLike = attrs.field(converter=UUID)

    post: Hash = attrs.field(converter=hash_from_str)

    content: str = attrs.field(validator=post_content_validator)
