from django.db import models
from django.urls import reverse
from uuslug import uuslug


class Plan(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, db_index=True)
    author = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='plans/images')
    file = models.FileField(upload_to='plans/files')
    date_pub = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='plans', blank=True)

    def get_absolute_url(self):
        return reverse('plan_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self, start_no=2)
        super(Plan, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self, start_no=2)
        super(Tag, self).save(*args, **kwargs)
        # TODO Или удалить или реализовать форму добавления

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

