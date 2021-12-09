from django.shortcuts import render, redirect
from .models import Product, Contact, Customer
from math import ceil
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import base64
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from shop.forms import UserRegisterForm
#from shop.tokens import account_activation_token
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
# <<<<<<< HEAD
email = "k190292@nu.edu.pk"
# =======
email = "sohaibkhen@gmail.com"
# >>>>>>> 255f6d868542df49ce5e52f76d1e34367a673d89
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")
def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productview(request,myid):
    #fetch the product using Id
    product = Product.objects.filter(product_id=myid)
    print(product)

    return render(request,'shop/productview.html',{'product':product[0]})

def shoppingcart(request):
    return render(request,'shop/shoppingcart.html')
def checkout(request):
    return render(request,'shop/checkout.html')

def sale(request):
    return render(request,'shop/sale.html')
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             subject = 'Activate Your MySite Account'
#             message = render_to_string('account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)
#             return redirect('account_activation_sent')
#     else:
#         form = SignUpForm()
#     #return render(request, 'signup.html', {'form': form})
#     return render(request, 'shop/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # recipient_list = [email, ]
            # subject = "CONFIRMATION EMAIL"
            # email_from = settings.EMAIL_HOST_USER
            # message = "THIS EMAIL IS A CONFIRMATION EMAIL, THANKYOU FOR REGISTERATION !!"
            # send_mail(subject, message, email_from, recipient_list)
            sendemail(request)
            return render(request,'shop/login.html')
        else:
            form = UserRegisterForm()
            return render(request, 'shop/signup.html', {'form': form, 'title': 'reqister here'})





    # form = UserRegisterForm(request.POST)
        # if form.is_valid():
        #     user = form.save(commit=False)
        #     user.is_active = False
        #     user.save()
        #     username = form.cleaned_data.get('username')
        #     email = form.cleaned_data.get('email')
        #     current_site = get_current_site(request)
        #     subject = 'Activate Your MySite Account'
        #     message = render_to_string('shop/account_activation_email.html', {
        #         'user': user,
        #         'domain': current_site.domain,
        #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #         'token': account_activation_token.make_token(user),
        #     })
        #     user.email_user(subject, message)
        #     subject = 'Thank you for registering to our site'
        #     message = ' it means much to us '
        #     email_from = settings.EMAIL_HOST_USER
        #     recipient_list = [email]
        #     send_mail(subject, message, email_from, recipient_list)
            # return redirect('shop/account_activation_sent.html')
    else:
        form = UserRegisterForm()
    return render(request, 'shop/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'shop/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')
def sendemail(request):

        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail(subject, message, email_from, recipient_list)
        return render(request,'shop/sendemail.html')