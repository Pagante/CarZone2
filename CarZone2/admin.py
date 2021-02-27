from django.contrib import admin
from .models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def Thumbnail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:50%" />'.format(object.car_photo.url))

    Thumbnail.short_description = 'Car Image'
    list_display = ('id','Thumbnail', 'car_title','city','color','model','year','body_style','fuel_type','is_featured')
    list_display_links = ('id','Thumbnail',  'car_title', 'model')
    list_editable = ('is_featured',)
    search_fields = ('id','car_title','model','city','body_style','fuel_type')
    list_filter = ('model','city','fuel_type')


admin.site.register(Car, CarAdmin)


