from django.contrib import admin

from demo_app.models import Entry

# Register your models here.
admin.site.register(Entry)
admin.site.site_header = 'Warish khan'
