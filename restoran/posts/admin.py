from django.contrib import admin

from .models import *

class restoransAdmin(admin.ModelAdmin):
    list_display = ('name',  )



class personAdmin(admin.ModelAdmin):
    list_display = ('name','last_name', 'patronymic', )




admin.site.register(person, personAdmin)
admin.site.register(restorans, restoransAdmin)
admin.site.register(Score)
