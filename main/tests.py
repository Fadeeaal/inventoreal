from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        # Create a sample item for testing
        self.item = Item.objects.create(
            name="Test Item",
            category="Diamond helmet",
            price=1000,
            amount=5,
            description="This is a test item for unit testing."
        )

    def test_item_creation(self):
        """Test if the item was created correctly."""
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.category, "Test Category")
        self.assertEqual(self.item.price, 1000)
        self.assertEqual(self.item.amount, 10)
        self.assertEqual(self.item.description, "This is a test item for unit testing.")

    def test_item_description_optional(self):
        """Test that an item can be created without a description."""
        item_without_description = Item.objects.create(
            name="Item Without Description",
            category="Another Category",
            price=500,
            amount=5
        )
        self.assertEqual(item_without_description.description, "")

    def test_item_update(self):
        """Test updating an item's attributes."""
        self.item.name = "Updated Name"
        self.item.category = "Updated Category"
        self.item.price = 1500
        self.item.amount = 20
        self.item.description = "Updated description for the item"
        self.item.save()

        updated_item = Item.objects.get(pk=self.item.pk)

        self.assertEqual(updated_item.name, "Updated Name")
        self.assertEqual(updated_item.category, "Updated Category")
        self.assertEqual(updated_item.price, 1500)
        self.assertEqual(updated_item.amount, 20)
        self.assertEqual(updated_item.description, "Updated description for the item")