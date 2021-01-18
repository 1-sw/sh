import config
import vk_api

num = config.number
pwd = config.pwd

vk_session = vk_api.VkApi(num,pwd)
vk_session.auth()

vk = vk_session.get_api()

print(vk.wall.post(message='Hello world!'))
