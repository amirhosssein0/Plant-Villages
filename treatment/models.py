from django.db import models

# Create your models here.

class TreatmentUpload(models.Model):
    photo = models.ImageField(upload_to='plant_uploads/')
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    task_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Upload {self.id} at {self.uploaded_at}"
