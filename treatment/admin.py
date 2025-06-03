from django.contrib import admin
from .models import TreatmentUpload

# Register your models here.

@admin.register(TreatmentUpload)
class TreatmentUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'description')
    search_fields = ('description',)
    list_filter = ('uploaded_at',)
