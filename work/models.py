from django.db import models

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length = 250, default="")
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length = 250);

    def __str__(self):
        return self.title
