from .models import DrePublication, DrePublicationType
from django.contrib import admin

class DrePublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'type', 'part', 'summary')
    search_fields = ('id', 'date', 'type', 'part', 'summary')
    list_filter = ('date', 'type', 'part')
    ordering = ('date',)
    readonly_fields = ('id',)
    
class DrePublicationTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    ordering = ('name',)
    readonly_fields = ('id',)
    
    
admin.site.register(DrePublication, DrePublicationAdmin)
admin.site.register(DrePublicationType, DrePublicationTypeAdmin)