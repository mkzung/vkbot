#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="bda38e39964ee711bc8f2a8c67cac684644abbb88389ee3b71d3aca2e431a66c05e6ddaa09b255154c923")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "привет":
                send_some_msg (id, "Привет Вездекодерам!")