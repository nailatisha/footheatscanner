import uuid
from django.db import models

class ScanResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    temperature = models.FloatField()
    status = models.CharField(max_length=50)
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
