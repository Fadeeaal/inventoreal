from django.shortcuts import render

def show_item(request):
    context = {
        'name': 'Diamond Sword',
        'category': 'Weapon',
        'price' : 1000,
        'amount' : 5,
        'description' : 'A legendary weapon known for its exceptional sharpness and stunning craftsmanship. Crafted from the world\'s most precious gem, it is a symbol of ultimate power, capable of effortlessly cutting through any obstacle or foe.'
    }

    return render(request, "main.html", context)