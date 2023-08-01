from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from .models import (
    Category,
    Subcategory,
    Attribute,
    AttributeOption,
    Product,
    ProductPrice,
    ProductStock,
    ProductImage,
    ProductCarrossel,
)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code",)
    prepopulated_fields = {"slug": ("code",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Attribute)
admin.site.register(AttributeOption)
#admin.site.register(Product)
admin.site.register(ProductPrice)
admin.site.register(ProductStock)
admin.site.register(ProductImage)
admin.site.register(ProductCarrossel)

'''class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 0

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        if db_field.name == 'category':
            kwargs = Category.objects.filter()
        else:
            pass

        return super(SubcategoryInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

class InningCardAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]

admin.site.register(SubcategoryInline, InningCardAdmin)'''




#from .models import (
#    Contact,
#    ContactSubject,
#    NewsLetter,
#)

#class ContactResource(resources.ModelResource):
#    class Meta:
#        model = Contact
#        exclude = ('imported', )
#        fields = ('name', 'email', 'phone', 'subject', 'message', 'terms')
#        export_order = ('name', 'email', 'phone', 'subject', 'message', 'terms')

#class ContactAdmin(ExportMixin, admin.ModelAdmin):
#    resource_class = ContactResource
#    to_encoding = 'utf-8'

#    def has_add_permission(self, request, obj=None):
#        return False

#admin.site.register(Contact, ContactAdmin)
#admin.site.register(ContactSubject)