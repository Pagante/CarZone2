from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def Thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%" />'.format(object.photo.url))

    Thumbnail.short_description = 'Image'
    list_display = ('id', 'Thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'Thumbnail', 'first_name',)
    list_filter = ('designation',)

    search_fields = ('id', 'first_name', 'last_name', 'designation')
admin.site.register(Team, TeamAdmin)



