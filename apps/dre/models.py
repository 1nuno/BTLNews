from django.db import models

class DrePublication(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    type = models.ForeignKey('DrePublicationType', on_delete=models.CASCADE)
    part = models.CharField(max_length=255)
    summary = models.TextField()
    body = models.TextField()
    
    def __str__(self):
        return self.summary
    
    class Meta:
        verbose_name = "DRE Publication"
        verbose_name_plural = "DRE Publications"
        
        
class DrePublicationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "DRE Publication Type"
        verbose_name_plural = "DRE Publication Types"