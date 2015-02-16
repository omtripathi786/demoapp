__author__ = 'Om'
from django import forms
from sms.models import Students, Courses, UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-lg',
                                                                 'placeholder': 'Password'}))
    email = forms.EmailField(max_length=75, required=True, widget=forms.TextInput(attrs={'class':
                                                                                             'form-control input-lg',
                                                                                         'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'User Name'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website',)
        widgets = {
            'website': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'Website'}),
        }
