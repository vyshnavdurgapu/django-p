from django.db import models

# Create your models here.

class numbers(models.Model):
    number = models.IntegerField(default=0)
    numbertext=models.TextField(default='waw')
    def __str__(self):
        return (str(self.number)+self.numbertext)[:10]
