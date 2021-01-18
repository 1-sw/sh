import modules.VK
import config
import vk_api

num = config.number
pwd = config.pwd

vk = VK(num,pwd)
vk = vk.GET_API()

print(vk.wall.post(message='Hello world!'))
