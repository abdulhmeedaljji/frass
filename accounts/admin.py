from django.contrib import admin
from .models import CustomUser,File,ArchiveFile,Archivetender ,Choice ,Subscription,tender,Type_tender
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Subscription)
admin.site.register(tender)
admin.site.register(Choice)
admin.site.register(File)
admin.site.register(ArchiveFile)
admin.site.register(Archivetender)

admin.site.register(Type_tender)





