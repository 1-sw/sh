import vk_api

class VK:

  def __init__(self,num,pwd):
    print(__class__+" : inited!")
    self.num = num
    self.pwd = pwd
    SESSION  = vk_api.VkApi(num,pwd)
    self.SESSION.auth()
    self.API = self.SESSION.get_api()

  def GET_API(self):
    print(__class__+"->GET_API : called")
    return self.API




