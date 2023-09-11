from django.shortcuts import render

def show_item(request):
    context = {
        'items': [
            {
                'name': 'Diamond Sword',
                'category': 'Weapon',
                'price': 1000,
                'amount': 1,
                'description': 'A legendary weapon known for its exceptional sharpness and stunning craftsmanship. Crafted from the world\'s most precious gem, it is a symbol of ultimate power, capable of effortlessly cutting through any obstacle or foe',
            },
            {
                'name': 'Golden Sword',
                'category': 'Weapon',
                'price': 500,
                'amount': 3,
                'description': 'A melee weapon crafted from precious metal. While it\'s not the most durable or powerful choice, its unique feature is its ability to be enhanced with magical properties, making it a preferred option for those seeking to add special effects to their attacks or looking for a stylish and ornate weapon',
            },
            {
                'name': 'Iron Sword',
                'category': 'Weapon',
                'price': 200,
                'amount': 5,
                'description': 'A strong and durable weapon crafted from iron. It is widely favored for its effectiveness in close combat and is often used to fend off hostile creatures and protect against various threats in a pixelated world of adventures',
            },
            {
                'name': 'Wooden Sword',
                'category': 'Weapon',
                'price': 100,
                'amount': 10,
                'description': 'A primitive weapon made from a wooden shaft and a blade carved from wood. While it lacks the sharpness and durability of metal weapons, it can serve as a last resort for self-defense in situations where more advanced weapons are unavailable. Its simplicity and ease of crafting make it a practical choice for survival in the wilderness or during a desperate struggle',
            },
        ]
    }

    return render(request, "main.html", context)