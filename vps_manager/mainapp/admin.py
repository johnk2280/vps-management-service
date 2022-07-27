from django.contrib import admin

from .models import VPS


class VPSAdmin(admin.ModelAdmin):
    search_fields = fields = (
        'uid',
        'cpu',
        'ram',
        'hdd',
        'status',
        'created_at',
        'updated_at',
    )
    list_display = (
        'uid',
        'cpu',
        'ram',
        'hdd',
        'status',
        'created_at',
        'updated_at',
    )


admin.site.register(VPS, VPSAdmin)
