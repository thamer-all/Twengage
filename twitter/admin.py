from django.contrib import admin
from twitter import models

admin.site.register(models.Message)


class OrderAdmin(admin.ModelAdmin):
    search_fields = ("twitter_username", "paypal_email", "paypal_name",)
    list_display = ("twitter_username", "twitter_password", "order_active", "paypal_name", "paypal_email")
    list_per_page = 100
    

admin.site.register(models.Order, OrderAdmin)