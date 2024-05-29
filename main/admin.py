from django.contrib import admin
from .models import Admin, Category, Product, FeedbackMessage, Order, OrderItem

admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(FeedbackMessage)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'total_price', 'created_at')
    inlines = [OrderItemInline]