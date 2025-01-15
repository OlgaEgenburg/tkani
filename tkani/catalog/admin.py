from django.contrib import admin


from .models import Category, Item, Subcategory


class ItemAdmin(admin.ModelAdmin):
    """Custom of admin zone."""

    list_display = (
        'title',
        'text',
        'is_published',
        'is_new',
        'category',
        'subcategory',
        'image',
    )
    list_editable = (
        'is_published',
        'is_new',
    )
    search_fields = ('title',)
    list_display_links = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    """Custom of admin zone."""

    list_display = (
        'id',
        'title',
        'description',
        'slug',
        'image',
    )

    search_fields = ('title',)
    list_display_links = ('title',)

class SubcategoryAdmin(admin.ModelAdmin):
    """Custom of admin zone."""

    list_display = (
        'id',
        'title',
        'description',
        'slug',
        'category',
        'image',
    )

    search_fields = ('title',)
    list_display_links = ('title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)