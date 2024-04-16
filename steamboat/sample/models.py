from django.db import models


class Sample(models.Model):
    """
    A sample is a unique unit that can multiple entries associated with it.
    """

    name = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
