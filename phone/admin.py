from django.contrib import admin

from .models import signin

admin.site.site_header = 'TISB Phone Administration'
#Retrieve app accounts 
@admin.register(signin)
class invoiceAdmin(admin.ModelAdmin):
    list_display = ("cid",'signin','signout','signedin')
    list_filter = ("cid",)
    search_fields = ("cid__startswith",)