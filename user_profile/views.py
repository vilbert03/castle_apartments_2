from django.shortcuts import render
from django.http import HttpResponse

user_profiles = [
    {
        'user_name': 'Jón Jónsson',
        'user_email': 'jon@example.com',
        #'user_password': '<PASSWORD>',
        'user_phone_number': '615 8923',
        #user_profile
    },
    {
        'user_name': 'Jón Sigurðsson',
        'user_email': 'siggi@example.com',
        #'user_password': '<PASSWORD>',
        'user_phone_number': '581 2345',
        #user_profile
    }
]

def index(request):
    return render(request, 'profile/profiles.html', {
            "user_profiles": user_profiles
    })

def profile_view(request):
    user = {
        'user_name': 'Jón Jónsson',
        'user_email': 'jon@example.com',
        'user_phone_number': '615 8923',
    }
    return render(request, 'profile/profiles.html', {'user': user})

