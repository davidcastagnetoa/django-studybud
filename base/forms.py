from django.forms import ModelForm
from .models import Room
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email']


# For user Profile Image
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']
