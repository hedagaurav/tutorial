from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
# models are similar to tables in database.

class UserRegistrationModel(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.username + ' Registered'


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=100, default='')
#     city = models.CharField(max_length=100, default='')
#     website = models.URLField(default='')
#     phone = models.IntegerField(default=0)
#
#     def create_profile(sender, **kwargs):
#
#         if kwargs['created']:
#             user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
#     post_save.connect(create_profile, sender=User)
