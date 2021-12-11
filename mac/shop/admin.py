from django.contrib import admin
from .models import *
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Invoice)
admin.site.register(Feedback)
admin.site.register(SignIn)
admin.site.register(History)

# Register your models here.
