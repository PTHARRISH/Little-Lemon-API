from django.db import models

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
# The Category model has two fields: slug and title.
# slug-Used to create human-readable URLs for category pages.
# title-Contains the category's name.
# __str__-Returns the category's title when the model instance is printed.
# This method is used to display the category's title in the Django admin interface.

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default=1)

    def __str__(self):
        return self.title
