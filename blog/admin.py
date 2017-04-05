from django.contrib import admin

# Register your models here.
from blog.models import sites,bigsites,imageload

class sitesadmin(admin.ModelAdmin):
	list_display=("siteid","sitename")

class imageloadadmin(admin.ModelAdmin):
	list_display=("imagename","imagetext")
		

admin.site.register(sites,sitesadmin)
admin.site.register(bigsites)
admin.site.register(imageload,imageloadadmin)