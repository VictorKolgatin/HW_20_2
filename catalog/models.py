from django.db import models, connection

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    overview = models.TextField(verbose_name='описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name, self.overview}'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    overview = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='категория')
    purchase_price = models.IntegerField(verbose_name='цена покупки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.overview}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')
