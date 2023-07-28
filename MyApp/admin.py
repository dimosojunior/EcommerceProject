from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'company_name', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email','username', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login','company_name')
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'password1', 'password2'),
        }),
    )

    ordering=('email',)
class CategoryAdmin(admin.ModelAdmin):
	list_display =["CategoryName", "link","recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["CategoryName","link"]

class ProductsCategoryAdmin(admin.ModelAdmin):
	list_display =["CategoryName", "link","recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["CategoryName","link"]




class ProductsAdmin(admin.ModelAdmin):
	list_display =["ProductName", "ProductPrice","ProductDiscountPrice","ProductPackage","ProductQuantity","ProductStatus", "recorded_at","updated_at"]
	list_filter = ["recorded_at", "updated_at"]
	search_fields = ["ProductName","ProductPackage"]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["user", "item", "quantity", "ordered"]
    #form = StockCreateForm
    #list_filter =['category']
    search_fields = ['user', 'item']

class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "start_date", "ordered_date","ordered"]
    #form = StockCreateForm
    #list_filter =['category']
    search_fields = ['user', 'item']


class ContactMeAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "place","phone","send_date"]
    #form = StockCreateForm
    #list_filter =['category']
    search_fields = ['username', 'email']

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'street_address',
        'apartment_address',
        #'country',
        'zip',
        'default'
    ]
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(ProductsCategory, ProductsCategoryAdmin)

admin.site.register(Products, ProductsAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ContactMe, ContactMeAdmin)

admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Address, AddressAdmin)
admin.site.register(PrivacyPolicy)
admin.site.register(Ask)