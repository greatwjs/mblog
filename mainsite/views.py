 # -*- coding: UTF-8 -*-
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,User,Yanzheng
from .forms import LoginForm
from django.template.loader import get_template
from datetime import datetime
from django.template import RequestContext
from mblog.settings import APIKEY
from .yunpian import YunPian
import re,random,uuid
from mainsite.dysms_python.demo_sms_send import send_sms
# Create your views here.


def sendcode(self,request):
    mobile=request.POST.get('mobile','')
    if mobile:
      #验证是否为有效手机号
      mobile_pat=re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
      res=re.search(mobile_pat,mobile)
      if res:
        #生成手机验证码
        code=random.randint(1000,9999)
        yunpian=YunPian(APIKEY)
        sms_status=yunpian.send_sms(code=code,mobile=mobile)
        msg=sms_status.msg
        return HttpResponse(msg)
      else:
        msg='请输入有效手机号码!'
        return HttpResponse(msg)
    else:
      msg='手机号不能为空！'
      return HttpResponse(msg)

def login(request):
    if request.method=='POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():      #检查输入是否正确
            login_name=request.POST['username'].strip() #获取用户输入的值
            login_password=request.POST['password']
            try:
               user=User.objects.get(name=login_name)
               if user.password==login_password:
                   response=redirect('/')
                   request.session['username']=user.name   #设置session
                   request.session.set_expiry(0)
                   return redirect('/')
               else:
                    message="密码错误,请检查一次"
            except:
                message="用户不存在,请先注册"
        else:
            message="请检查输入的字段内容"
    else:
        login_form=LoginForm()  #产生一个新的窗体实例

    template=get_template('login.html')
    request_context=RequestContext(request)
    request_context.push(locals())
    html=template.render(request_context)
    return HttpResponse(html)

def sendsms(request):
    mobile=request.POST.get('mobile','')
    if mobile:
      #验证是否为有效手机号
      mobile_pat=re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
      res=re.search(mobile_pat,mobile)
      if res:
        #生成手机验证码
        business_id=uuid.uuid()
        phone_numbers=mobile
        sign_name="明日博客"
        template_code="SMS_134150087"
        code=random.randint(1000,9999)
        params = {code}
        sms_status=send_sms(business_id, phone_numbers, sign_name, template_code,params)
        msg=sms_status.msg
        return HttpResponse(msg)
      else:
        msg='请输入有效手机号码!'
        return HttpResponse(msg)
    else:
      msg='手机号不能为空！'
      return HttpResponse(msg)

def zhuce(request):
    if request.method=='POST':
        zhuce_form=zhuceForm(request.POST)
        if zhuce_form.is_valid():      #检查输入是否正确
                zhuce_name=request.POST['username'].strip() #获取用户输入的值
                zhuce_password=request.POST['password']
                zhuce_password2=request.POST['password2']
                user=User.objects.values('name')
                if zhuce_name in user:
                    message="该用户名已存在"
                else:
                   if zhuce_password==zhuce_password2:
                      User.objects.create(name=zhuce_name,password=zhuce_password,enabled=False)
                      response=redirect('/login')
                      return redirect('/login')
                   else:
                     message="密码不一致,请重新输入"
        else:
            message="请检查输入的字段内容"
    else:
        zhuce_form=zhuceForm()  #产生一个新的窗体实例

    template=get_template('zhuce.html')
    request_context=RequestContext(request)
    request_context.push(locals())
    html=template.render(request_context)
    return HttpResponse(html)
def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post!=None:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
def ceshi(request):
     mobile=request.POST.get('mobile','')
     code=random.randint(1000,9999)
     yunpian=YunPian('ce2040e4d754c28a84fb69aa415598c9')
     sms_status=yunpian.send_sms(code=code,mobile=mobile)
     return HttpResponse(mobile)