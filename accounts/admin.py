from django.contrib import admin
from .models import CustomUser,File ,Choice ,Subscription,tender
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Subscription)
admin.site.register(tender)
admin.site.register(Choice)
admin.site.register(File)





