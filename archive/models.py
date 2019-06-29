from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, db_index=True)
    author = models.CharField(max_length=50, blank=True)


class PlanImage(models.Model):
    subject = models.ForeignKey(Plan, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
