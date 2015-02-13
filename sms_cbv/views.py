from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from django.template import loader

class UserLogin(View):
    template_name = "sms_cbv/login.html"

    def get(self, request, *args, **kwargs):
        msg = ''
        return HttpResponse(render(request, self.template_name, {'msg': msg}))

    def post(self, request, *args, **kwargs):
        print 'check'
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                msg = 'done'
            else:
                msg = 'fail'

        return HttpResponse(render(request, self.template_name, {'msg': msg}))




