from rest_framework import serializers
from .models import Dataset, DataElement

class DataElementSerializer(serializers.ModelSerializer): #Serializer for DataElements
    class Meta:
        model = DataElement
        fields = [
            "id",
            "dataset",
            "name",
            "description",
            "data_type",
            "is_required",
            "is_pii",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"] #Set automatically from server
    

class ElementNestedSerializer(serializers.ModelSerializer): #Nested serializer for POST (dataset comes from the URL)
    class Meta:
        model = DataElement
        fields = [
            "name",
            "description",
            "data_type",
            "is_required",
            "is_pii",
        ]


class DatasetSerializer(serializers.ModelSerializer): #Dataset Serializer 
    class Meta:
        model = Dataset
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"] #Set automatically from server


class DatasetALLSerializer(DatasetSerializer): # return Dataset with DataElements
    elements = DataElementSerializer(many=True, read_only=True)

    class Meta(DatasetSerializer.Meta):
        fields = DatasetSerializer.Meta.fields + ["elements"] #used for GET (includes nested elements)
