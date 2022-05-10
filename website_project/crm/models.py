from django.db import models

# Create your models here.
class Order(models.Model):
    """Таблица в БД"""

    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    def __str__(self):
        """Представление в списке"""

        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


