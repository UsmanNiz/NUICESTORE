from django.shortcuts import render, redirect
from .models import *
from math import ceil
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import base64
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
# from shop.forms import UserRegisterForm
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
# from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
email = "k190292@nu.edu.pk"

def signin(request):
    chk = signincheck.objects.get(sid=1)
    if (chk.sign):
        if request.method == "POST":
            if 'add' in request.POST:
                chk.sign = False
                signincheck.objects.filter(sid=1).delete()
                SignIn.objects.all().delete()
                chk = signincheck(sid=1)
                chk.save()
                return render(request,'shop/signin.html')

        return render(request,'shop/alreadysign.html')
    else:
        if request.method == "POST":
            print("I AM REQUEST", request)
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            iter = Customer.objects.all()
            for i in iter:
                if email == i.email and password == i.password:
                    signinn = SignIn(customer_id_id=i.customer_id)
                    signinn.save()
                    chk = signincheck.objects.get(sid=1)
                    chk.sign = True
                    chk.save()
                    return redirect('/shop/')
                    # return render(request,'shop/index.html')

    return render(request, 'shop/signin.html')


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
    print("THIS IS REQUEST")
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


def shoppingcart(request):
    if request.method == "POST":
        Invoice.objects.all().delete()
        if 'add' in request.POST:
            c = request.POST.get('add')
            # prod = Product.object.filter(product_id = c)
            cartchk = Cart.objects.filter(product_id=c).first() #yeh keh rha hai k agar database is id ki koi cheez tou if main ghuss jaou
            if cartchk:
                print("already added")
                cartchk.quantity = cartchk.quantity + 1
                cartchk.save()
        elif 'rem' in request.POST:
            c = request.POST.get('rem')
            cartchk = Cart.objects.filter( product_id=c).first()  # yeh keh rha hai k agar database is id ki koi cheez tou if main ghuss jaou
            if cartchk.quantity == 1:
                Cart.objects.filter(product_id=c).delete()
            elif cartchk:
                print("already added")
                cartchk.quantity = cartchk.quantity - 1
                cartchk.save()
            cart = Cart.objects.all()
            if not cart:
                return redirect('/shop/')
        elif 'del' in request.POST:
            c = request.POST.get('del')
            Cart.objects.filter(product_id=c).delete()
            cart = Cart.objects.all()
            if not cart:
                return redirect('/shop/')
    cart = Cart.objects.all()
    if not cart:
        return redirect("/shop/")
    print("I AM CART ", cart[0].product_id.price)
    total = 0
    for i in cart:
        total = total + i.product_id.price * i.quantity
    print(total)
    length = len(cart)
    params = {'cart' : cart , 'total': total , 'length' : length }
    return render(request,'shop/shoppingcart.html', params )



def TY_page(request):
    invoice = Invoice.objects.all()
    history = History
    for i in invoice:
        History(customer_id_id=i.customer_id_id,
                product_id_id=i.cart_id.product_id_id,
                quantity=i.cart_id.quantity
                ).save()
    Cart.objects.all().delete()
    return render(request, 'shop/TY_page.html')

def checkout(request):
    chk = signincheck.objects.get(sid=1)
    chk_inv = Invoice.objects.all()
    if (chk.sign):
        if request.method == "POST":
            print('asd')
        date=datetime.date.today()
        carts = Cart.objects.all()
        total = 0
        # cart = []
        signinn = SignIn.objects.all()
        # return HttpResponse(signinn[0].customer_id_id)
        if not bool(chk_inv):
            for i in carts:
                inv = Invoice(customer_id_id = signinn[0].customer_id_id, cart_id_id = i.cart_id, amount = i.quantity * i.product_id.price)
                inv.save()
                # cart = Cart.object.get("product_id": i.product_id)
                # total = total + i.product_id.price * i.quantity
        for i in carts:
            total = total + i.product_id.price * i.quantity
        # return HttpResponse(Invoice.objects.all())
        invoice = Invoice.objects.all()
        # history = History
        #
        # for i in invoice:
        #     History(customer_id_id = i.customer_id_id,
        #             product_id_id = i.cart_id.product_id_id,
        #             quantity =i.cart_id.quantity
        #             ).save()
        # # return  HttpResponse(History.objects.all())
        name =signinn[0].customer_id.name
        cust = Customer.objects.get(name=name)
        params ={ 'cart' : carts , 'total' : total, 'cust':cust,'date':date,'invoice' : invoice }
        return render(request,'shop/checkout.html',params)
    else:
        return render(request,'shop/signin.html')

def productview(request,myid):
    #fetch the product using Idass
    product = Product.objects.filter(product_id=myid)
    print(product)
    if request.method == "POST":
        print(request.POST.get('name'))
        if 'add' in request.POST:
            print(request)
            cartchk = Cart.objects.filter(product_id=myid).first() #yeh keh rha hai k agar database is id ki koi cheez tou if main ghuss jaou
            if cartchk:
                print("already added")
                cartchk.quantity = cartchk.quantity + 1
                cartchk.save()

            else:
                print("not added")
                VarProductId = Product.objects.get(product_id=myid)
                print(id)
                Cart_instance = Cart.objects.create(product_id=VarProductId, quantity=1)    #yeh nhi chal raha
                Cart_instance.save()
        else:
            cartchk = Cart.objects.filter(product_id=myid).first()  # yeh keh rha hai k agar database is id ki koi cheez tou if main ghuss jaou
            if cartchk and cartchk.quantity > 1:
                print("already added")
                cartchk.quantity = cartchk.quantity - 1
                cartchk.save()
            else:
                 Cart.objects.filter(product_id=myid).delete()




    return render(request,'shop/productview.html',{'product':product[0]})


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
    if request.method=="POST":
        print("I AM REQUEST",request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address', '')
        password=request.POST.get('password', '')
        iter = Customer.objects.all()
        for i in iter:
            if email == i.email:
                return redirect('/shop/userexist')
        customer = Customer(name=name, email=email, address=address, password=password)
        customer.save()

    return render(request, 'shop/signup.html')

def exist(request):
    return render(request,'shop/userexist.html')

    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         email = form.cleaned_data.get('email')
    #         sendemail(request)
    #         return render(request,'shop/login.html')
    #     else:
    #         form = UserRegisterForm()
    #         return render(request, 'shop/signup.html', {'form': form, 'title': 'reqister here'})





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
    # else:
    #     form = UserRegisterForm()
    # return render(request, 'shop/signup.html', {'form': form})


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