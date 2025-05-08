from django.shortcuts import render
from django.http import HttpResponse

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
        'seller_id': 1,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_name': 'Davíð',
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },
    {
        'id': 2,
        'name': 'fagragrund 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'seller_id': 1,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_name': 'Davíð',
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 3,
        'name': 'fagragrund 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'seller_id': 1,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_name': 'Davíð',
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 4,
        'name': 'fagragrund 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'seller_id': 1,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_name': 'Davíð',
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 5,
        'name': 'fagragrund 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'seller_id': 1,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_name': 'Davíð',
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 6,
        'name': 'fagragrund 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'seller_id': 1,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_name': 'Davíð',
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },

    {
        'id': 7,
        'name': 'fagragrund 12',
        'city': 'Reykjavík',
        'postal_code': 108,
        'description': 'bla bla bla',
        'type': 'house',
        'price': '45.000.000',
        'listing_date': '2019-09-22',
        'on_sale': True,
        'seller_id': 1,
        'nr_rooms': 2,
        'nr_square_meters': 100,
        #sellerInformation
        'seller_name': 'Davíð',
        #image of the seller
        #a link to sellers profile page
        'image': 'https://c.arvakur.is/m2/nyicJBddS9X0JV9NyL0M3vkONhc=/x867/smart/fs-pool/e9/e9df53fc64afcdfc950828443ed79095fb1cee3c.jpg'
    },
]


# Create your views here.
def index(request):
    return render(request, "property/properties.html", {
        "properties": properties
    })

def get_property_by_id(request, id):
    prop = [x for x in properties if x['id'] == id][0]
    return render(request, 'property/properties_detail_page.html', {
        "property": prop
    })

