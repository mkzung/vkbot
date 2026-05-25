#!/usr/bin/env python3
"""Minimal VK longpoll echo bot.

Replies to a few hard-coded Russian phrases. Originally written as a
first-week experiment with the `vk_api` package; kept here as a tiny
reference for VK longpoll boilerplate.

Configuration
-------------
Set the `VK_API_TOKEN` environment variable with a user or community
access token issued by your VK Apps page. Do NOT commit the token —
the public repo previously had a hard-coded token; that token has
been revoked.

Usage
-----
    export VK_API_TOKEN=...
    python vkbot.py
"""

from __future__ import annotations

import os
import sys

import vk_api
from vk_api.longpoll import VkEventType, VkLongPoll


def main() -> int:
    token = os.environ.get("VK_API_TOKEN")
    if not token:
        sys.stderr.write(
            "ERROR: VK_API_TOKEN is not set. Export the token first:\n"
            "  export VK_API_TOKEN=<your-vk-access-token>\n"
        )
        return 1

    vk_session = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(vk_session)

    def reply(user_id: int, text: str) -> None:
        vk_session.method(
            "messages.send",
            {"user_id": user_id, "message": text, "random_id": 0},
        )

    for event in longpoll.listen():
        if event.type != VkEventType.MESSAGE_NEW or not event.to_me:
            continue
        msg = event.text.lower()
        user_id = event.user_id
        if msg == "привет":
            reply(user_id, "Привет!")
        elif msg == "пока":
            reply(user_id, "Пока!")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
