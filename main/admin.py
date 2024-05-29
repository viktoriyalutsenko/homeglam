from django.contrib import admin
from .models import Admin, Category, Product, FeedbackMessage, Order, OrderItem
from django.core.mail import send_mail

admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(FeedbackMessage)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'total_price', 'status', 'created_at')
    list_filter = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('customer_name', 'customer_email', 'total_price', 'status', 'response')
        }),
        ('Дата', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        # Проверяем, был ли изменен статус заказа
        if obj.status != obj.original_status:
            # Сохраняем текущий статус как original_status
            obj.original_status = obj.status

            # Отправляем email-сообщение в зависимости от нового статуса
            if obj.status == 'approved':
                subject = 'Ваш заказ одобрен'
                message = f'Здравствуйте, {obj.customer_name}!\n\nВаш заказ на сумму {obj.total_price} рублей одобрен. Мы свяжемся с вами для дальнейшего оформления.'
            elif obj.status == 'rejected':
                subject = 'Ваш заказ отклонен'
                message = f'Здравствуйте, {obj.customer_name}!\n\nК сожалению, ваш заказ на сумму {obj.total_price} рублей отклонен. {obj.response}'

            # Отправляем email-сообщение
            send_mail(
                subject=subject,
                message=message,
                from_email='your_email@example.com',
                recipient_list=[obj.customer_email],
            )

        # Вызываем родительский метод save_model, чтобы сохранить изменения в модели
        super().save_model(request, obj, form, change)