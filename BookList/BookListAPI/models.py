from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]


# indexes Attribute:
# The indexes attribute in the Meta class specifies custom database indexes for the model.

# models.Index:
# models.Index is a Django class that represents a database index.
# An index is a data structure used by the database to improve the speed of operations, 
# such as querying and sorting, on specific columns.
# This defines the field or fields for which the index is created. 
# In this case, it’s the price field of the model.
# The index ensures that queries involving the price field 
# (e.g., filtering, ordering) are executed faster by the database.
# books = Book.objects.filter(price__gt=20).order_by('price')
# The index on price makes this query faster, especially for large datasets.

# Benefits of Indexing
#     Faster Query Execution: Queries involving the price field will be executed faster 
#                             because the database can locate rows more efficiently using the index.
#     Improved Sorting: Sorting by price will also benefit from the index.