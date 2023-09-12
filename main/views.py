from django.shortcuts import render

def show_item(request):
    context = {
        'creator' : 'Rakha Fadil Atmojo',
        'npm' : 2206082985,
        'pbpclass' : 'PBP C',
        'items': [
            {
                'name': 'Diamond Sword',
                'category': 'Weapon',
                'price': 1000,
                'amount': 1,
                'description': 'A rare gem-forged blade, renowned for its unmatched sharpness and exquisite artistry, can effortlessly conquer any obstacle.',
            },
            {
                'name': 'Golden Sword',
                'category': 'Weapon',
                'price': 500,
                'amount': 3,
                'description': 'A gilded melee weapon, not the sturdiest but enchantment-friendly. Preferred by those seeking style and magical flair.',
            },
            {
                'name': 'Iron Sword',
                'category': 'Weapon',
                'price': 200,
                'amount': 5,
                'description': 'A sturdy iron weapon favored for close combat, defending against threats and hostile creatures.',
            },
            {
                'name': 'Wooden Sword',
                'category': 'Weapon',
                'price': 100,
                'amount': 10,
                'description': 'A basic wooden weapon, less sharp and durable than metal, but a practical last resort for self-defense in the wild or emergencies.',
            },
        ]
    }

    return render(request, "main.html", context)