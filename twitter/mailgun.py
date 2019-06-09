from twitter import db_handler
from django.template.loader import get_template

import requests
import uuid
import random

subjects = [
    "Grow your twitter with twengage",
    "Natural twitter growth with twengage",
    "Twengage twitter growth service",
    "Swell your twitter presence with twengage",
    "Expand your twitter presence",
    "Advance your twitter with twengage",
]

def sendMail(email):
    emailTemplate = get_template("email_template_1.html")
    context = {
        "random_ids": [str(uuid.uuid4()) for i in range(5, 50)]
    }
    emailHtml = emailTemplate.render(context)
    # print(emailHtml)
    # request.user.set_password(password)
    mailgunAuth = ("api", "key-a210026bd7bbfec1f34654efb2bc4e37")
    mailgunData = {
                    "from": "Twengage: Twitter Growth<notification@mail.twengage.com>",
                    "to": [email],
                    # "to": ["katchystore@gmail.com"],
                    "subject": random.choice(subjects),
                    "html": emailHtml,
                }
        #
    mailgunApiUrl = "https://api.mailgun.net/v3/mail.twengage.com/messages"
    signupEmail = requests.post(mailgunApiUrl, auth=mailgunAuth, data=mailgunData)
    print(signupEmail)
    print(signupEmail.text)
    return None


sendMail('support@twengage.com')