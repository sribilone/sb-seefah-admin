from django.contrib import admin

# Register your models here.

from .models import server_conf,dim_sale_ordertransaction

admin.site.register(server_conf)
admin.site.register(dim_sale_ordertransaction)
