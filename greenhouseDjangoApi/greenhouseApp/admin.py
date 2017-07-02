from django.contrib import admin

# Register your models here.

from greenhouseApp.models import SensorsEntry

admin.site.register({
	SensorsEntry
})
