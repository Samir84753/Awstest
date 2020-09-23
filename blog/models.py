from django.db import models

# Create your models here.
class sitemsg(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=50)
    user_email=models.EmailField(max_length=25)
    user_msg=models.CharField(max_length=200)