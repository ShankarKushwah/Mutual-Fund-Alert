from django.db import models


class Register_as_Guest(models.Model):
    email_id = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Register_Full(models.Model):
    full_name = models.CharField(max_length=50)
    emailid = models.EmailField()
    contact = models.BigIntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


