
from django.db import models
class DataSource(models.Model): 
    name = models.CharField(max_length=200) 
    url = models.URLField() 
    data_tag = models.CharField(max_length=100)

class ScrapedData(models.Model): 
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE) 
    content = models.TextField() 
    sentiment = models.CharField(max_length=50) 
    timestamp = models.DateTimeField(auto_now_add=True)
