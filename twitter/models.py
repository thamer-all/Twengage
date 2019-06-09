from django.db import models

import uuid


class Order(models.Model):
    def __str__(self):
        return str(self.twitter_username) + " : " + str(self.order_active)

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField("Contact Email", max_length = 200, default=None, blank=True, null=True)
    paypal_email = models.CharField("Paypal Email", max_length=200, default=None, blank=True, null=True)
    paypal_name = models.CharField("Paypal Full Name", max_length=200, default=None, blank=True, null=True)
    twitter_email = models.CharField("Twitter Email", max_length=200, default=None, blank=True, null=True)
    twitter_username = models.CharField("Twitter Username", max_length=200, default=None, blank=True, null=True)
    twitter_phone = models.CharField("Twitter Phone Number", max_length=200, default=None, blank=True, null=True)
    twitter_password = models.CharField("Twitter Password", max_length=200, default=None, blank=True, null=True)
    hashtags = models.TextField("Hashtags", max_length=1000, default=None, blank=True, null=True)
    similar_users = models.TextField("Similar Users", max_length=1000, default=None, blank=True, null=True)
    order_id = models.CharField("Order Id", max_length=200, default=None, blank=True, null=True)
    package_id = models.CharField("Package Id", max_length=200, default=None, blank=True, null=True)
    txn_id = models.CharField("Transaction Id", max_length = 300, default=None, blank=True, null=True)
    order_active = models.BooleanField("Order Active", default=False)
    updated_timestamp = models.DateTimeField("Last Updated At", auto_now=True, null=True)
    created_timestamp = models.DateTimeField("Created At", auto_now_add=True, null=True) 


class Message(models.Model):
    def __str__(self):
        return self.name + " : " + self.email

    name = models.CharField("Name", max_length = 200, default=None, blank=True, null=True)
    email = models.CharField("Email", max_length = 200, default=None, blank=True, null=True)
    message = models.TextField("Message", max_length = 2000, default=None, blank=True, null=True)
