from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


    #prerequisite to ensure that stock is not negative and availability is either True or False
    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(stock__gte=0),
                name='stock_non_negative_constraint'
            ),
            models.CheckConstraint(
                check=models.Q(availability__in=[True, False]),
                name='availability_constraint'
            )
        ]

    def __str__(self):
        return self.name