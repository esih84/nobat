from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from nobat.models import MyUser


class profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="pr")
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    photo = models.URLField(blank=True)


def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=MyUser)


class Create_Services(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE , related_name="service")
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class photo(models.Model):
    user = models.ForeignKey(profile, on_delete=models.CASCADE, related_name="service")
    photo = models.URLField()

