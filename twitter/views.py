from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import auth as djangoAuth

from twitter import models
from twitter import db_handler
from twitter import ipn_handler

import threading
import json
import uuid



def home(request):
    return render(request, "home.html", context={})

def faq(request):
    return render(request, "faq.html", context={})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")   
        print(name, email, message)     
        # Create Message
        message_obj = models.Message(
                                    name = name,
                                    email = email,
                                    message = message,
                        )
        message_obj.save()        
        return redirect("/")
    return render(request, "contact.html", context={})

def email_template(request):
    return render(request, "signup-email.html", context={})

# def privacy(request):
#     return render(request, "privacy.html", context={})

def thankyou(request):
    signupEmail = request.session.get("signup_email")
    if not signupEmail:
        signupEmail = ""
    context = {
        "signupEmail" : signupEmail
    }
    return render(request, "thankyou.html", context=context)

def packages(request):
    return render(request, "packages.html")

def order(request):
    if request.method == "POST":
        email = request.POST["email"]
        twitter_username = request.POST["twitter_username"]
        order_id = request.session.get("order_id")
        if not order_id:
            print("Generating new order id")
            order_id = db_handler.create_order_id()
        package_id = request.POST.get("package_id")
        print(email, twitter_username, order_id)
        if not db_handler.create_order(order_id, email, twitter_username, package_id):
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    elif request.method == "GET":
        order_id = db_handler.create_order_id()
        request.session["order_id"] = order_id
        package = request.GET.get("package")
        if package == "1":
            print("First Package")
            request.session["package_id"] = "WEEK"
        elif package == "2":
            request.session["package_id"] = "MONTH"
            print("Second Package")
        context = {
            "package_id": request.session.get("package_id"),
            "custom": order_id,
        }
        return render(request, "order.html", context=context)

def order_details(request):
    print("here")
    if request.method == "POST":
        order_id = request.session.get("order_id")
        hashtags = request.POST["hashtags"]
        similar_users = request.POST["similar_users"]
        twitter_email = request.POST["twitter_email"]
        twitter_phone = request.POST["twitter_phone"]
        twitter_password = request.POST["twitter_password"]
        package_id = request.session.get("package_id")
        print(order_id, hashtags, similar_users, twitter_email, twitter_phone, twitter_password, package_id)
        if not db_handler.update_order(order_id, hashtags, similar_users, twitter_email, twitter_phone, twitter_password):
            return HttpResponse(status=400)
        print("here")
        return HttpResponse(status=200)
    return render(request, "order_details.html", context={})



def help(request):
    return render(request, "help.html", context={})
# def support(request):
#     if request.method == "GET":
#         return render(request, "support.html", context={})
#     elif request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")        
#         # Create Message
#         message_obj = models.Message(
#                                     name = name,
#                                     email = email,
#                                     message = message,
#                         )
#         message_obj.save()        
#         return HttpResponse(status=200)
#     return HttpResponse(status=400)

    
