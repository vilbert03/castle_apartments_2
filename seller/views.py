from django.shortcuts import render
from django.http import HttpResponse

sellers = [
    {
        'id': 1,
        'name': 'gunni',
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg',
        'type': 'individual',
        'description': 'Gunni is a seasoned property owner with experience in rentals.'
    },
    {
        'id': 2,
        'name': 'halli',
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg',
        'type': 'agency',
        'description': 'Halli runs a real estate agency in Reykjavik.'
    },
]

def index(request):
    return render(request, "seller/sellers.html", {
        "sellers": sellers
    })

def get_seller_by_id(request, id):
    seller = next((x for x in sellers if x['id'] == id), None)
    if not seller:
        return HttpResponse("Seller not found", status=404)
    return render(request, "seller/seller_detail.html", {
        "seller": seller
    })