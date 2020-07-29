"""
Definition of models.
"""

from django.db import models

class User(models.Model):
    fullname = models.CharField(verbose_name = "Full name", max_length = 50)
    photo_path = models.CharField(verbose_name = "Link to avatar", max_length = 255)
    gender = models.CharField(verbose_name = "Gender", max_length = 6)
    birthdate = models.DateField(verbose_name = "Birth date")
    address = models.TextField(verbose_name = "Address")


class Telephone(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    teletype = models.CharField(verbose_name = "Type", max_length = 4)
    telenumber = models.CharField(verbose_name = "Number", max_length = 12)

    def __str__(self):
        return self.user

class Email(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    mailtype = models.CharField(verbose_name = "Type", max_length = 4)
    email = models.EmailField(verbose_name = "E-mail")

    def __str__(self):
        return self.user




