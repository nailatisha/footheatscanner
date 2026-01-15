from django.db import models

class ScanResult(models.Model):
    REGION_CHOICES = [
        ('heel', 'Heel'),
        ('arch', 'Arch'),
        ('toe', 'Toe'),
    ]

    temperature = models.FloatField()
    region = models.CharField(max_length=10, choices=REGION_CHOICES)

    delta_temp = models.FloatField(default=0)
    confidence = models.FloatField(default=0)

    diagnosis = models.CharField(max_length=150)
    status = models.CharField(max_length=100)

    image = models.ImageField(upload_to='scans/', null=True, blank=True)

    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.region} - {self.diagnosis}"
from django.db import models

class Scan(models.Model):
    source = models.CharField(max_length=20)
    image = models.ImageField(upload_to='scans/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ThermographicFeature(models.Model):
    scan = models.OneToOneField(Scan, on_delete=models.CASCADE)
    mean_temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    delta_temp_left_right = models.FloatField()

class FootRegionAnalysis(models.Model):
    scan = models.ForeignKey(Scan, on_delete=models.CASCADE)
    region = models.CharField(max_length=10)
    mean_temp = models.FloatField()
    delta_temp = models.FloatField()

class AIPrediction(models.Model):
    scan = models.OneToOneField(Scan, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=20)
    confidence = models.FloatField()
    model_version = models.CharField(max_length=50)

class ExplainabilityMap(models.Model):
    scan = models.OneToOneField(Scan, on_delete=models.CASCADE)
    heatmap_image = models.ImageField(upload_to='heatmaps/')
    overlay_image = models.ImageField(upload_to='overlays/')
