from django.urls import path,include
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("",views.index, name = "Shop Home"),
    path("contact/",views.contact, name = "Contact US"),
    path("about/",views.about, name = "About"),
    path("tracker/",views.tracker, name = "Tracking Status"),
    path("search/",views.search, name = "Search"),
    path("productview/<int:myid>",views.productview, name = "Product"),
    path("checkout/",views.checkout, name = "Checkout"),
    path("sale/",views.sale, name="Sale"),
    path("signup/",views.signup, name='signup'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path("sendemail",views.sendemail,name='sendemail')
]
