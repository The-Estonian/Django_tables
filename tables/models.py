from django.db import models
from django.db.models import (
    CASCADE,
    Model, 
    ForeignKey,
    DateTimeField,
    FloatField,
    IntegerField,
    DateField,
    TextField,
    )
# Create your models here.

class Sales(Model):
    Region = TextField(max_length=255)
    Country = TextField(max_length=255)
    Item_type = TextField(max_length=255)
    Sales_channel = TextField(max_length=255)
    Order_priority = TextField(max_length=255)
    Order_date = DateField()
    Order_id = IntegerField()
    Ship_date = DateField()
    Units_sold = IntegerField()
    Unit_price = FloatField()
    Unit_cost = FloatField()
    Total_revenue = FloatField()
    Total_cost = FloatField()
    Total_profit = FloatField()

    class Meta:
        verbose_name_plural = "Sales journal entries"