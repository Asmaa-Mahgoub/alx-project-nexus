from django.contrib import admin
from .models import Notification
# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=('user','type','message','is_read','created_at')
    search_fields=('user__username','message','type') #is_read is boolean → not searchable
    list_filter = ('type', 'is_read')
    ordering=('-created_at',)
