from django.db import models
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from easy_thumbnails.fields import ThumbnailerImageField
from mptt.models import MPTTModel, TreeForeignKey

class Catalog(MPTTModel):
    en_name = models.CharField(max_length=64)
    sp_name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    photo = ThumbnailerImageField(upload_to="catalog_pic", blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.en_name

    @models.permalink
    def get_absolute_url(self):
        return ('zakai.views.view_catalog', [str(self.slug)])

class Product(models.Model):
    en_name = models.CharField(max_length=100)
    sp_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    catalog = models.ForeignKey(Catalog)

    en_description = models.TextField(blank=True, help_text="Describe product in english")
    sp_description = models.TextField(blank=True, help_text="Describe product in spanish")
    photo = ThumbnailerImageField(upload_to="product_pic", blank=True)

    def __unicode__(self):
        return self.en_name

    @models.permalink
    def get_absolute_url(self):
        return ('zakai.views.view_product', [str(self.slug)])

@receiver(post_delete, sender=Catalog)
def delete_filefield(sender, **kwargs):
    try:
        image = kwargs.get('instance')
        storage = image.photo.storage
        storage.delete(image.photo.path)
    except Exception:
        pass

@receiver(post_delete, sender=Product)
def delete_filefield(sender, **kwargs):
    try:
        image = kwargs.get('instance')
        storage = image.photo.storage
        storage.delete(image.photo.path)
    except Exception:
        pass