from django.db import models

class Guy(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name