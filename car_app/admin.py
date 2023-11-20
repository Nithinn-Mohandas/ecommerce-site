from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(upload_product)
admin.site.register(reg_seller)
admin.site.register(reg_buyer)
admin.site.register(wish)
admin.site.register(cart)
admin.site.register(delivery_address)
admin.site.register(details_full)