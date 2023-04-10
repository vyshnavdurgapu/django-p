from django.db import models

# Create your models here.
class grocery(models.Model):
    Name = models.CharField(max_length=25,null=False)
    typrchoices=[
        ('o','oil'),
        ('g','grain'),
        ('c','cosmetics')
    ]
    type = models.CharField(max_length=1,choices=typrchoices)
    quantity=models.IntegerField()
    rate = models.IntegerField()
    amount = models.IntegerField()