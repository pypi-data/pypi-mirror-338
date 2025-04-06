# Copyright (c) 2025 Osyah
# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__: typing.Sequence[str] = ("to_dict",)

import typing

from classes import typeclass

from pletyvo.protocol.dapp.event import (
    AuthHeader,
    EventInput,
    Event,
    EventResponse,
)
from pletyvo.protocol.delivery.channel import (
    Channel,
    ChannelCreateInput,
    ChannelUpdateInput,
)
from pletyvo.protocol.delivery.message import (
    Message,
    MessageCreateInput,
    MessageUpdateInput,
)
from pletyvo.protocol.delivery.post import (
    Post,
    PostCreateInput,
    PostUpdateInput,
)

from typing import Any


###
# to_dict
###


@typeclass
def to_dict(instance) -> dict: ...


@to_dict.instance(AuthHeader)
def _to_dict_dapp_auth_header(instance: AuthHeader):
    from base64 import b64encode

    return {
        "sch": instance.sch,
        "pub": b64encode(instance.pub).decode(),
        "sig": b64encode(instance.sig).decode(),
    }


@to_dict.instance(EventInput)
def _to_dict_dapp_event_input(instance: EventInput):
    return {
        "body": str(instance.body),
        "auth": to_dict(instance.auth),
    }


@to_dict.instance(Event)
def _to_dict_dapp_event(instance: Event):
    return {
        "id": str(instance.id),
        "body": str(instance.body),
        "auth": to_dict(instance.auth),
    }


@to_dict.instance(EventResponse)
def _to_dict_dapp_event_response(instance: EventResponse):
    return {
        "id": str(instance.id),
    }


@to_dict.instance(Channel)
def _to_dict_delivery_channel(instance: Channel) -> dict[str, Any]:
    return {
        "id": str(instance.id),
        "hash": str(instance.hash),
        "author": str(instance.author),
        "name": str(instance.name),
    }


@to_dict.instance(ChannelCreateInput)
def _to_dict_delivery_channel_create_input(
    instance: ChannelCreateInput,
) -> dict[str, Any]:
    return {
        "name": instance.name,
    }


@to_dict.instance(ChannelUpdateInput)
def _to_dict_delivery_channel_update_input(
    instance: ChannelUpdateInput,
) -> dict[str, Any]:
    return {
        "name": instance.name,
    }


@to_dict.instance(Message)
def _to_dict_delivery_message(instance: Message) -> dict[str, Any]:
    return {
        "body": instance.body,
        "auth": to_dict(instance.auth),
    }


@to_dict.instance(MessageCreateInput)
def _to_dict_delivery_message_create_input(
    instance: MessageCreateInput,
) -> dict[str, Any]:
    return {
        "channel": str(instance.channel),
        "content": instance.content,
    }


@to_dict.instance(MessageUpdateInput)
def _to_dict_delivery_message_update_input(
    instance: MessageUpdateInput,
) -> dict[str, Any]:
    return {
        "message": str(instance.message),
        "channel": str(instance.channel),
        "content": instance.content,
    }


@to_dict.instance(Post)
def _to_dict_delivery_post(instance: Post) -> dict[str, Any]:
    return {
        "id": str(instance.id),
        "hash": str(instance.hash),
        "author": str(instance.author),
        "channel": str(instance.channel),
        "content": instance.content,
    }


@to_dict.instance(PostCreateInput)
def _to_dict_delivery_post_create_input(
    instance: PostCreateInput,
) -> dict[str, Any]:
    return {
        "channel": str(instance.channel),
        "content": instance.content,
    }

@to_dict.instance(PostUpdateInput)
def _to_dict_delivery_post_update_input(
    instance: PostUpdateInput,
) -> dict[str, Any]:
    return {
        "channel": str(instance.channel),
        "post": str(instance.post),
        "content": instance.content,
    }
