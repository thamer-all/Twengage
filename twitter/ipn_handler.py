from twitter import models
from django.template.loader import get_template

import requests
import uuid

PAYPAL_EMAIL = "melimg0694@gmail.com"


PACKAGES = {
                   "WEEK" : {"cost" : "9.99", "likes": 500},
                   "MONTH" : {"cost" : "26.99", "likes": 1000},
            }

def parser(ipn_data_dic):	
    print("Parsing Ipn Message")
    custom = ipn_data_dic.get("custom")
    txn_type = ipn_data_dic.get("txn_type") 
    txn_id = ipn_data_dic.get("txn_id")                   #None for trials
    receiver_email = ipn_data_dic.get("receiver_email") 
    item_name = ipn_data_dic.get("item_name")              
    mc_currency = ipn_data_dic.get("mc_currency")	
    payer_first_name = ipn_data_dic.get("first_name")	
    payer_last_name = ipn_data_dic.get("last_name")	
    payer_email = ipn_data_dic.get("payer_email")	
    payer_id = ipn_data_dic.get("payer_id")	
    subscr_id = ipn_data_dic.get("subscr_id")	
    #
    if PAYPAL_EMAIL == receiver_email:
        print("Email check passed, merchant email verified")								
        if txn_type == "subscr_signup":
            print("New Subscription for Twengage")
            print("Here is the uuid " + str(custom))
            mc_amount3 = ipn_data_dic.get("mc_amount3")	
            order_obj = list(models.Order.objects.filter(order_id=custom))
            if order_obj:
                order_obj = order_obj[0]
                order_obj.paypal_name = str(payer_first_name) + " " + str(payer_last_name)
                order_obj.paypal_email = payer_email
                order_obj.order_active = True
                order_obj.txn_id = str(txn_id)
                order_obj.save()
                try:
                    print("Sending email to : " + str(order_obj.email))
                    sendMail(order_obj)
                except Exception as e:
                    print(e)
        #					
        elif txn_type == "subscr_cancel":
            order_obj = list(models.Order.objects.filter(order_id=custom))
            if order_obj:
                order_obj = order_obj[0]
                order_obj.order_active = False
                order_obj.save()





def sendMail(order_obj):
    emailTemplate = get_template("signup-email.html")
    context = {
        "username" : order_obj.twitter_username
    }
    emailHtml = emailTemplate.render(context)
    # print(emailHtml)
    # request.user.set_password(password)
    mailgunAuth = ("api", "key-a210026bd7bbfec1f34654efb2bc4e37")
    send_to_emails = ["support@twengage.com", order_obj.email]
    for each_email in send_to_emails:
        mailgunData = {
                        "from": "Twengage Order Confirmation<do-not-reply@mail.twengage.com>",
                        "to": [each_email],
                        # "to": ["katchystore@gmail.com"],
                        "subject": "Welcome To Twengage.com!",
                        "html": emailHtml,
                    }
            #
        mailgunApiUrl = "https://api.mailgun.net/v3/mail.twengage.com/messages"
        signupEmail = requests.post(mailgunApiUrl, auth=mailgunAuth, data=mailgunData)
        print(signupEmail)
        print(signupEmail.text)
    return None




