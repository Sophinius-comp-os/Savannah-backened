from rest_framework.test import APITestCase
from ..models import Customer, Order
from ..serializers import CustomerSerializer, OrderSerializer

class CustomerSerializerTests(APITestCase):
    def test_valid_serializer(self):
        """Test that the CustomerSerializer validates correctly with valid data."""
        valid_data = {
            'name': 'Test Customer',
            'code': 'TC001',
            'phone': '1234567890'
        }
        serializer = CustomerSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid(), msg="Serializer should be valid with correct data.")
        self.assertEqual(serializer.validated_data['name'], valid_data['name'])

    def test_invalid_serializer(self):
        """Test that the CustomerSerializer returns errors with invalid data."""
        invalid_data = {
            'name': '',
            'code': 'TC001',
            'phone': ''
        }
        serializer = CustomerSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid(), msg="Serializer should be invalid with empty fields.")
        self.assertIn('name', serializer.errors)  # Check for error on 'name'
        self.assertIn('phone', serializer.errors)  # Check for error on 'phone'
        

class OrderSerializerTests(APITestCase):
    def setUp(self):
        """Create a customer instance for use in order tests."""
        self.customer = Customer.objects.create(name='Test Customer', code='TC001', phone='1234567890')

    def test_valid_serializer(self):
        """Test that the OrderSerializer validates correctly with valid data."""
        valid_data = {
            'customer': self.customer.id,
            'item': 'Test Item',
            'amount': '10.00'
        }
        serializer = OrderSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid(), msg="Serializer should be valid with correct data.")
        self.assertEqual(serializer.validated_data['item'], valid_data['item'])

    def test_invalid_serializer(self):
        """Test that the OrderSerializer returns errors with invalid data."""
        invalid_data = {
            'customer': self.customer.id,
            'item': '',
            'amount': '10.00'
        }
        serializer = OrderSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid(), msg="Serializer should be invalid with empty item field.")
        self.assertIn('item', serializer.errors)  # Check for error on 'item'
