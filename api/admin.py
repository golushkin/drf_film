from django.contrib import admin
from .models import Man

class ManAdmin(admin.ModelAdmin):
    class Meta:
        model = Man
        display_list = ('first_name','last_name','date_of_born')

admin.site.register(Man, ManAdmin)