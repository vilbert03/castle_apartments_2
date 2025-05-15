from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from user_profile.forms.profile_form import ProfileForm
from user_profile.models import UserProfile
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'user/register.html', {
        'form': form
    })


@login_required
def profile_view(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('my_profile')
        else:
            messages.error(request, "There was an error when updating your profile")
    else:
        form = ProfileForm(instance=user_profile, user=request.user)


    return render(request, 'user/my_profile.html', {
        'form': form,
    })

