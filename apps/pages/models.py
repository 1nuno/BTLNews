from django.db import models

class DreData(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    type = models.CharField(max_length=255)
    part = models.CharField(max_length=255)
    summary = models.TextField()
    body = models.TextField()

    class Meta:
        db_table = 'dre_data'

