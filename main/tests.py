from django.test import TestCase
from .models import Item

class ItemModelTestCase(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name="Diamond sword",
            category="Weapon",
            price=500,
            amount=5,
            description="The Diamond Sword is a legendary weapon known for its exceptional sharpness and stunning craftsmanship. Crafted from the world's most precious gem, it is a symbol of ultimate power, capable of effortlessly cutting through any obstacle or foe."
        )

