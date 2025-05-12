from django.shortcuts import render
from django.http import HttpResponse
from seller.views import sellers

properties = [
    {
        'id': 1,
        'name': 'fagragrund 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_id': 2,
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },
    {
        'id': 2,
        'name': 'momo 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_id': 1,
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 3,
        'name': 'hinn 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_id': 2,
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 4,
        'name': 'kalli 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_id': 1,
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 5,
        'name': 'nagla 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_id': 2,
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 6,
        'name': 'brarar 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_id': 1,
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 7,
        'name': 'hagar 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_id': 2,
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },
]

seller_map = {s['id']: s for s in sellers}

for p in properties:
    p['seller'] = seller_map.get(p['seller_id'])

# Create your views here.
def index(request):
    return render(request, "property/properties.html", {
        "properties": properties
    })


def get_property_by_id(request, id):
    prop = next((x for x in properties if x['id'] == id), None)
    if not prop:
        return HttpResponse("Property not found", status=404)

    prop['seller'] = seller_map.get(prop['seller_id'])

    return render(request, 'property/properties_detail_page.html', {
        "property": prop
    })
