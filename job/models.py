# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255, unique=True, blank=True)

  def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super().save(*args, **kwargs)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ('title',)

class Job(models.Model):
  category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  position_salary = models.CharField(max_length=255)
  position_location = models.CharField(max_length=255)
  company_name = models.CharField(max_length=255)
  company_location = models.CharField(max_length=255)
  company_email = models.EmailField()
  created_at = models.DateTimeField(default=timezone.now)
  created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE, default=1)

  class Meta:
    ordering = ('-created_at',)

  def created_at_formatted(self):
    return defaultfilters.date(self.created_at, 'M d, Y')

  def __str__(self):
    return self.title