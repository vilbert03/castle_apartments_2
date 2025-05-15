from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from user_profile.models import UserProfile


class ProfileForm(ModelForm):
    username = forms.CharField(label="Username", max_length=200)

    class Meta:
        model = UserProfile
        exclude = ['user', 'id']
        widgets = {
            'profile_image': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = user.username
        self.user_instance = user

    def save(self, commit=True):
        self.user_instance.username = self.cleaned_data['username']
        if commit:
            self.user_instance.save()
            profile = super().save(commit=False)
            profile.user = self.user_instance
            profile.save()
        return self.user_instance.userprofile
