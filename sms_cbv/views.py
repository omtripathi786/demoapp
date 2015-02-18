from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from sms_cbv.forms import UserForm, UserProfileForm
from django.template import loader, RequestContext


class UserLogin(View):
    """
        This is a class based view to handle login and authentication
    """
    template_name = "sms_cbv/login.html"

    def get(self, request, *args, **kwargs):
        msg = ''
        return HttpResponse(render(request, self.template_name, {'msg': msg}))

    def post(self, request, *args, **kwargs):
        msg = ''
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user
        if user:
            if user.is_active:
                msg = 'done'
            else:
                msg = 'fail'
        else:
            msg = 'fail'
        return HttpResponse(render(request, self.template_name, {'msg': msg}))


class UserRegistration(View):
    """
        This is a class based view to handle user registration
    """
    template_name = "sms_cbv/register.html"

    def get(self, request, *args, **kwargs):
        msg = ''
        user_form = UserForm()
        profile_form = UserProfileForm()
        context = {
            'msg': msg,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return HttpResponse(render(request, self.template_name, context))

    def post(self, request, *args, **kwargs):
        msg = ''
        registered = False
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            user_form.errors, profile_form.errors

        context = {
            'msg': msg,
            'user_form': user_form,
            'profile_form': profile_form,
            'registered' : registered
        }
        return HttpResponse(render(request, self.template_name, context))

