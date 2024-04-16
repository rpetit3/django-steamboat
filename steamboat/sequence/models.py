from django.db import models
from sample.models import Sample


# Create your models here.
class Sequence(models.Model):
    """
    A sequence is a unique sequencing event can multiple entries associated with it.
    """

    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey("Platform", on_delete=models.CASCADE)
    strategy = models.ForeignKey("Strategy", on_delete=models.CASCADE)
    source = models.ForeignKey("Source", on_delete=models.CASCADE)
    selection = models.ForeignKey("Selection", on_delete=models.CASCADE)


class Platform(models.Model):
    """
    The platform is the instrument used to generate sequencing data. The naming should
    follow the naming utilized by NCBI.
    """

    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class Strategy(models.Model):
    """
    The strategy is the sequencing strategy used to generate the sequencing data. The
    naming should follow the naming utilized by NCBI.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()


class Source(models.Model):
    """
    The source is the biological source of the sequencing data. The naming should follow
    the naming utilized by NCBI.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()


class Selection(models.Model):
    """
    The selection is the method used to select the biological material for sequencing.
    The naming should follow the naming utilized by NCBI.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
