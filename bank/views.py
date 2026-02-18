from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Dataset, DataElement
from .serializers import (
    DatasetSerializer,
    DatasetALLSerializer,
    DataElementSerializer,
    ElementNestedSerializer,
)

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all() # for list/retrieve/create/update/delete

    def get_serializer_class(self): #on retrieve use DatasetALLSerializer
        if self.action == "retrieve":
            return DatasetALLSerializer
        return DatasetSerializer

    @action(detail=True, methods=["get", "post"], url_path="elements")
    def elements(self, request, pk=None):
        dataset = self.get_object() # dataset id comes from URL

        if request.method == "GET": # list elements for this dataset
            qs = dataset.elements.all()
            return Response(DataElementSerializer(qs, many=True).data)

        serializer = ElementNestedSerializer(data=request.data) # nested create (no dataset in body)
        serializer.is_valid(raise_exception=True) # validate request

        element = DataElement.objects.create(dataset=dataset, **serializer.validated_data) 
        return Response(DataElementSerializer(element).data, status=status.HTTP_201_CREATED) # return created element 

class DataElementViewSet(viewsets.ModelViewSet):
    queryset = DataElement.objects.select_related("dataset").all() # include dataset in the same query
    serializer_class = DataElementSerializer
    search_fields = ["name", "description", "data_type", "dataset__name"] # Used for Search Filter
