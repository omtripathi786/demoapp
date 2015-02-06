from django.template import loader, RequestContext
from django.http import HttpResponse
from sms.models import Students
from sms.forms import StudentsForm, UserForm, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from sms.serializers import UserSerializer, GroupSerializer
# Create your views here.

def index(request):
    if request.user.is_authenticated():
        template = loader.get_template('index.html')
        sid = request.GET.get('sid', None)
        did = request.GET.get('delete', None)
        msg = ''
        action = 'Add'
        if request.method == 'POST':
            form = StudentsForm(request.POST)
            if form.is_valid() and request.POST.get('action') == 'Add':
                res = form.save()
                msg = 'Information Submitted Successfully.'
                form = StudentsForm()
            elif form.is_valid() and request.POST.get('action') == 'Update':
                obj = Students.objects.get(pk=sid)
                obj.name = request.POST.get('name')
                obj.roll_number = request.POST.get('roll_number')
                obj.roll_number = request.POST.get('roll_number')
                obj.email = request.POST.get('email')
                obj.courses_id = request.POST.get('courses')
                obj.save()
                form = StudentsForm()
                msg = 'Information Updated Successfully'
            else:
                form = StudentsForm()
                msg = 'Form Not Submitted.'
        else:
            form = StudentsForm()
            if sid:
                action = 'Update'
                row = Students.objects.get(pk=sid)
                form = StudentsForm(instance=row)
            elif did:
                row = Students.objects.get(pk=did)
                row.delete()
                form = StudentsForm()
                return redirect('/sms')
        student_list = Students.objects.order_by('name')
        context = RequestContext(request, {
            'msg': msg,
            'form': form,
            'student_list': student_list,
            'action': action
        })
        return HttpResponse(template.render(context))
    else:
        return redirect('/')


def user_login(request):
    msg = ''
    template = loader.get_template('login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/sms')
            else:
                msg = "Your account is disabled."
        else:
            msg = "Invalid login details supplied."
    context = RequestContext(request, {
        'msg': msg
    })
    return HttpResponse(template.render(context))


def register(request):
    msg = None
    template = loader.get_template('register.html')
    registered = False
    if request.method == 'POST':
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
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = RequestContext(request, {
        'msg': msg,
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })
    return HttpResponse(template.render(context))


def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

