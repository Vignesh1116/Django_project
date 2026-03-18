from django.db import models

# Create your models here.

class Category(models.Model):
    catrgory_name = models.CharField(max_length=50)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    cat_image = models.ImageField(upload_to='photos/category', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.catrgory_name
    