from django.contrib import admin
from .models import Product, ProductComponent, ProductVersion
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','product_code', 'status')
    search_fields=('name','product_code')
    list_filter=('status')
    ordering = ('name',)

@admin.register(ProductComponent)
class ProductComponentAdmin(admin.ModelAdmin):
    list_display=('component','quantity_used','product_version')

    #❌search_fields=('component','product_version') search_fields CANNOT search ForeignKeys directly

    search_fields = (
        'component__component_name',
        'product_version__version_no',
    )
    list_filter = ('product_version',)

@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display=('product','version_no','status','created_at')
    search_fields = (
        'product__name',
        'product__product_code',
        'version_no'
    )
    list_filter = ('status', 'product')
    ordering = ('-created_at',)

""" 🧠 Golden Rule
🔑 Admin search_fields NEVER accepts ForeignKey names
🔑 Always use related_model__field_name """