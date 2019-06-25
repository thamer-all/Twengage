

from twitter import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('email-template/', views.email_template),
    path('faq/', views.faq),
    path('order/', views.order),
    path('order/details/', views.order_details),
    path('packages/', views.packages),
    # path('privacy/', views.privacy),
    # path('support/', views.support),
    path('thankyou/', views.thankyou),
    path('paypal_callback/twengage_paypal_callback/', views.paypal_ipn_handler),
    path('howitworks/', views.help),
]
