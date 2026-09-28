from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    photo = models.ImageField(
        upload_to='users/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CardSale(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    card_quantity = models.PositiveIntegerField(default=1)

    price_per_card = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=50
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    sale_date = models.DateField(
        auto_now_add=True
    )

    sale_time = models.TimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        self.total_amount = (
            self.card_quantity * self.price_per_card
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.name} - {self.card_quantity} Cards"