# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-05-09 00:01:05
# @Last Modified by:   Marte
# @Last Modified time: 2018-05-11 21:44:42
import requests
class YunPian(object):
  def __init__(self,api_key):
    self.api_key=api_key
    self.single_send_url='https://sms.yunpian.com/v2/sms/single_send.json'

  def send_sms(self,code,mobile):
    parmas={
      'apikey':self.api_key,
      'mobile':mobile,
      'text':'【明日博客】感谢您注册#明日博客#，您的验证码是#code#'.format(code=code)
    }
    #text必须要跟云片后台的模板内容 保持一致，不然发送不出去！
    r=requests.post(self.single_send_url,data=parmas)
    print(r)

if __name__=='__main__':
  yun_pian=YunPian('***************（你的apikey）')
  yun_pian.send_sms('***（验证码）','*******（手机号）')