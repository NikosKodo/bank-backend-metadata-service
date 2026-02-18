from rest_framework import status
from rest_framework.test import APITestCase

from .models import Dataset, DataElement


class EndpointsTests(APITestCase): 
    def test_endpoint_create_dataset(self): #POST /api/datasets/
        url = "/api/datasets/"
        payload = {"name": "Customer", "description": "Customer dataset"}

        res = self.client.post(url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dataset.objects.count(), 1)
        self.assertEqual(Dataset.objects.get().name, "Customer")

    def test_endpoint_create_element(self): #POST /api/elements/

        dataset = Dataset.objects.create(name="Customer", description="Customer dataset")

        url = "/api/elements/"
        payload = {
            "dataset": dataset.id, 
            "name": "email",
            "description": "Customer email",
            "data_type": "email",
            "is_required": True,
            "is_pii": True,
        }

        res = self.client.post(url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DataElement.objects.count(), 1)

        element = DataElement.objects.get()
        self.assertEqual(element.dataset_id, dataset.id)
        self.assertEqual(element.name, "email")
