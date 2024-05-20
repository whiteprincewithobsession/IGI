from django.test import TestCase
from django.urls import reverse
from ..models import User

class ContactsViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='master1', is_master=True)
        User.objects.create(username='master2', is_master=True)
        User.objects.create(username='client', is_client=True) 

    def test_contacts_view(self):
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_view_context(self):
        response = self.client.get(reverse('contacts'))
        masters = response.context['masters']
        self.assertEqual(masters.count(), 2) 

    def test_contacts_view_no_clients(self):
        response = self.client.get(reverse('contacts'))
        clients = response.context['masters'].filter(is_client=True)
        self.assertFalse(clients.exists()) 
