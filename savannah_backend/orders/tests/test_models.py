from django.test import TestCase
from orders.models import Customer, Order

class CustomerModelTests(TestCase):
    """
    Unit tests for the Customer model.
    """

    def setUp(self):
        """
        Set up a test customer instance before each test.
        """
        self.customer = Customer.objects.create(
            name="John Doe",
            code="JD123",
            phone="1234567890"
        )

    def test_customer_creation(self):
        """
        Test that a customer can be created successfully.
        Verifies that the name, code, and phone fields
        are set correctly in the Customer model.
        """
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.code, "JD123")
        self.assertEqual(self.customer.phone, "1234567890")
        self.assertIsInstance(self.customer, Customer)

    def test_customer_str(self):
        """
        Test the string representation of a Customer instance.
        The __str__ method should return the name of the customer.
        """
        self.assertEqual(str(self.customer), "John Doe")

    def test_unique_code(self):
        """
        Test that the 'code' field is unique.
        Attempting to create a second customer with the same code
        should raise an exception due to the unique constraint.
        """
        with self.assertRaises(Exception):
            Customer.objects.create(
                name="Jane Doe",
                code="JD123",  # Duplicate code
                phone="0987654321"
            )


class OrderModelTests(TestCase):
    """
    Unit tests for the Order model.
    """

    def setUp(self):
        """
        Set up a test customer and order instance before each test.
        """
        self.customer = Customer.objects.create(
            name="John Doe",
            code="JD123",
            phone="1234567890"
        )
        self.order = Order.objects.create(
            customer=self.customer,
            item="Widget",
            amount=29.99
        )

    def test_order_creation(self):
        """
        Test that an order can be created successfully.
        Verifies that the customer, item, and amount fields
        are set correctly in the Order model.
        """
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.item, "Widget")
        self.assertEqual(self.order.amount, 29.99)
        self.assertIsInstance(self.order, Order)

    def test_order_str(self):
        """
        Test the string representation of an Order instance.
        The __str__ method should return a formatted string
        showing the item and amount of the order.
        """
        self.assertEqual(str(self.order), "Widget - 29.99")
