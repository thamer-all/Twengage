import os
import django
import io
import csv
import datetime
import uuid

from django.http import HttpResponse

os.environ['DJANGO_SETTINGS_MODULE'] = 'Twengage.settings'
django.setup()

from twitter.models import Message, Order

def create_order(order_id, email, twitter_username, package_id):
    order_obj = get_or_create_order(order_id)
    order_obj.email = email
    order_obj.twitter_username = twitter_username
    order_obj.package_id = package_id
    order_obj.save()
    return order_obj

def update_order(order_id, hashtags, similar_users, twitter_email, twitter_phone, twitter_password):
    order_obj = get_or_create_order(order_id)
    order_obj.hashtags = hashtags
    order_obj.similar_users = similar_users
    order_obj.twitter_email = twitter_email
    order_obj.twitter_phone = twitter_phone
    order_obj.twitter_password = twitter_password
    order_obj.save()
    return order_obj

def get_or_create_order(order_id):
    order_objs = Order.objects.filter(order_id=order_id)
    if order_objs:
        order_obj = order_objs[0]
    else:
        order_obj = Order(order_id=order_id)
    return order_obj

def create_order_id():
    order_id = str(uuid.uuid4())
    orders = Order.objects.filter(order_id=order_id)
    if orders.count() == 0:
        return order_id
    return create_order_id()