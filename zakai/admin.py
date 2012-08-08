from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from zakai.models import Catalog, Product

class CatalogAdmin(MPTTModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("en_name",)}

admin.site.register(Catalog, MPTTModelAdmin)
admin.site.register(Product)