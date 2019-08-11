from django import forms
from .models import Profile,Neighborhood,Business,Post
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','id','neighborhood','email')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighborhood']