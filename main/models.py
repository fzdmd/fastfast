from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    created_at = models.DateTimeField()
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    image = models.ImageField()
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    is_client = models.BooleanField()
    is_admin = models.BooleanField()
    is_active = models.BooleanField()
    token = models.CharField(max_length=300)
    restore = models.BooleanField()

class Email(models.Model):
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

class Status(models.Model):
    created_at = models.DateTimeField()
    arrange_id = models.IntegerField()
    status = models.IntegerField()

class Driver(models.Model):
    name = models.CharField(max_length=300)

class Parcel(models.Model):
    name = models.CharField(max_length=300)
    weight = models.CharField(max_length=300)

class Delivery(models.Model):
    types = models.IntegerField()
    pick_up_address = models.CharField(max_length=200)
    pick_up_companty_name = models.CharField(max_length=300)
    pick_up_unit_number = models.CharField(max_length=300)
    pick_up_lon = models.FloatField()
    pick_up_lat = models.FloatField()
    delivery_address = models.CharField(max_length=300)
    delivery_companty_name = models.CharField(max_length=300)
    dilivery_unit_number = models.CharField(max_length=300)
    delivery_lon = models.FloatField()
    delivery_lat = models.FloatField()
    back_to_pick_up_address = models.CharField(max_length=300)
    back_lon = models.FloatField()
    back_lat = models.FloatField()
    recipient = models.ForeignKey(User)
    imstructions = models.CharField(max_length=300)
    parcel_type = models.ForeignKey(Parcel)
    return_to = models.CharField(max_length=300)
    reason = models.CharField(max_length=300)
    favorites = models.BooleanField()
    delivery_status = models.CharField(max_length=300)
    driver = models.IntegerField()

class History(models.Model):
    created_at = models.DateTimeField()
    arrange_id = models.ForeignKey(Delivery)
