from django.db import models

#Dataset model
class Dataset(models.Model):
    name = models.CharField(max_length=100, unique=True) #must be unique
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

#DataElement model
class DataElement(models.Model):
    class DataType(models.TextChoices): #allowed data types
        STRING = "string", "String"
        INTEGER = "integer", "Integer"
        FLOAT = "float", "Float"
        BOOLEAN = "boolean", "Boolean"
        DATE = "date", "Date"
        DATETIME = "datetime", "DateTime"
        EMAIL = "email", "Email"

    dataset = models.ForeignKey(
        Dataset, #Delete dataset deletes all elements
        on_delete=models.CASCADE,
        related_name="elements"
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    data_type = models.CharField(max_length=20, choices=DataType.choices)
    is_required = models.BooleanField(default=False)

    is_pii = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["dataset", "name"], #Elements names unique in the same dataset
                name="unique_name",
            )
        ]
        
    def __str__(self) -> str:
        return f"{self.dataset.name}.{self.name}"
