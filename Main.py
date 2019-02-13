# Добро пожаловать
# Я ебанулся, делаю бота. Лиза привет.

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def write_msg(user_id, msg):
    vk.method('msg.send',{'user_id': user_id, 'msg': msg})


token = "8bfaa17a86f7948ce238728bf31f35dfef8934f2175f4744dd0e3d43cfbfc33a5f25a49a8bc3986313c67"

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if request == "начнем":
                write_msg(event.user_id, "Добро пожаловать")
            else:
                write_msg(event.user_id, "Sosi")
