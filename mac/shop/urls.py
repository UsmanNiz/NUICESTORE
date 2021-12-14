from django.urls import path,include
from . import views

from django.contrib.auth import views as auth_views
# from django.conf.urls import include,url
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index, name = "Shop Home"),
    path("contact/",views.contact, name = "Contact US"),
    path("about/",views.about, name = "About"),
    path("tracker/",views.tracker, name = "Tracking Status"),
    path("search/",views.search, name = "Search"),
    path("productview/<int:myid>",views.productview, name = "productview"),
    path("checkout/",views.checkout, name = "Checkout"),
    path("TY_page/",views.TY_page, name = "TY_page"),
    # path("floatingty/",views.TY_page, name = "TY_page"),
    path("sale/",views.sale, name="Sale"),
    path("signup/",views.signup, name='signup'),
    path("signin/", views.signin, name='signin'),
    # url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path("sendemail",views.sendemail,name='sendemail'),
    path("shoppingcart",views.shoppingcart, name = 'shoppingcart'),
    path("userexist",views.exist,name = 'userexist')
]
