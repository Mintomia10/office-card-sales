from django.contrib import admin
from .models import User, CardSale


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'created_at')
    search_fields = ('name', 'phone')


@admin.register(CardSale)
class CardSaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'card_quantity',
        'price_per_card',
        'total_amount',
        'sale_date',
        'sale_time',
    )

    search_fields = ('user__name',)
    list_filter = ('sale_date',)