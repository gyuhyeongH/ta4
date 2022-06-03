from django.db import models

# Create your models here.


class Drink(models.Model):
    class Meta:
        db_table = "drink"

    name = models.CharField(max_length=20, null=False)
    category = models.ManyToManyField('Category')
    Nutrition = models.CharField(max_length=256, null=False)
    Allergy = models.CharField(max_length=20, null=False)


class Category(models.Model):
    class Meta:
        db_table = "category"

    category_name = models.CharField(max_length=20)