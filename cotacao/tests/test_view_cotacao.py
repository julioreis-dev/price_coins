from django.test import TestCase, Client
from django.urls import reverse_lazy


class UploadCotationTest(TestCase):
    def setUp(self):
        self.form = {
            'date': '2021-04-16',
            'coin': 'EUR',
        }
        self.cliente = Client()

    def test_upload_cotation(self):
        response = self.cliente.post(reverse_lazy('insert:insert'), data=self.form)
        self.assertEquals(response.status_code, 200)
