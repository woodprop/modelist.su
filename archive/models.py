from django.db import models
from django.urls import reverse


class Plan(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, db_index=True)
    author = models.CharField(max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse('plan_detail_url', kwargs={'slug': self.slug})


class PlanImage(models.Model):
    subject = models.ForeignKey(Plan, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='plans/images')


class PlanFile(models.Model):
    subject = models.ForeignKey(Plan, related_name='file', on_delete=models.CASCADE)
    file = models.FileField(upload_to='plans/files')
