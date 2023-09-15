from django.contrib import admin

from .models import *
class MyModelAdmin(admin.ModelAdmin):
	pass


admin.site.register(NewCategoryContent,MyModelAdmin),
admin.site.register(NewCategory,MyModelAdmin),
admin.site.register(Offer,MyModelAdmin)
