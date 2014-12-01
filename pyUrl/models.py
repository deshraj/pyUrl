from django.db import models

class urldata(models.Model):
    url = models.CharField(max_length=100000)
    shortUrl = models.CharField(max_length=100)

# class Author(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()