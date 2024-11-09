from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from ..models import Customer, Order
from django.urls import reverse

class CustomerViewTests(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_customer_list_create(self):
        """Test the customer list create view."""
        response = self.client.post(reverse('customer-list-create'), data={
            'name': 'Test Customer',
            'code': 'TC001',
            'phone': '1234567890'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_retrieve_update_destroy(self):
        """Test the customer retrieve, update, and destroy view."""
        customer = Customer.objects.create(name='Test Customer', code='TC001', phone='1234567890')
        response = self.client.get(reverse('customer-retrieve-update-destroy', args=[customer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update customer
        response = self.client.put(reverse('customer-retrieve-update-destroy', args=[customer.id]), data={
            'name': 'Updated Customer',
            'code': 'TC002',
            'phone': '0987654321'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete customer
        response = self.client.delete(reverse('customer-retrieve-update-destroy', args=[customer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class OrderViewTests(APITestCase):
    def setUp(self):
        # Create a user and authenticate
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        # Create a customer for order tests
        self.customer = Customer.objects.create(name='Test Customer', code='TC001', phone='1234567890')

    def test_order_list_create(self):
        """Test the order list create view."""
        response = self.client.post(reverse('order-list-create'), data={
            'customer': self.customer.id,
            'item': 'Test Item',
            'amount': '10.00'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order_retrieve_update_destroy(self):
        """Test the order retrieve, update, and destroy view."""
        order = Order.objects.create(customer=self.customer, item='Test Item', amount='10.00')
        response = self.client.get(reverse('order-retrieve-update-destroy', args=[order.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update order
        response = self.client.put(reverse('order-retrieve-update-destroy', args=[order.id]), data={
            'customer': self.customer.id,
            'item': 'Updated Item',
            'amount': '20.00'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete order
        response = self.client.delete(reverse('order-retrieve-update-destroy', args=[order.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
