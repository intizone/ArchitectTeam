from django.contrib import admin
from .models import Product, Message, Solution, Client, Member


admin.site.register(Product)
admin.site.register(Message)
admin.site.register(Client)
admin.site.register(Member)
admin.site.register(Solution)
