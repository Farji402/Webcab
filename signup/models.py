from django.db import models

class Janta(models.Model):
    outlook_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    dp = models.ImageField(upload_to = 'profile pictures/', default = "profile photo")

    def __str__(self):
        return self.user_name

