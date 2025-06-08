from django.db import models
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() # Use TextField for larger text content
    created_at = models.DateTimeField(default=timezone.now) # Automatically to now when the object is first [created]

    # Define a string representation for the model
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"  # Use "Entries" instead of "Entry" for plural form