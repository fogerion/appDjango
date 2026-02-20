from os import name
from django.db import models

# Create your models/таблицы here.

class Categories(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name='URL'
    )

    class Meta:
        db_table = 'category'
        verbose_name ='Категорию'
        verbose_name_plural = 'Категории'

class Products(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Название товара'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name='URL'
    )
    description = models.TextField(
        blank=True,
        null = True,
        verbose_name= 'Описание товара',
    )
    image = models.ImageField(
        upload_to='goods_images', 
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='Цена товара'
    )
    discount= models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='скидка в процентах'
    )
    quantity =models.PositiveIntegerField(
        default=0, 
        verbose_name ='Количество'
    )

    category = models.ForeignKey(
        to=Categories,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    class Meta:
        db_table = 'product'
        verbose_name ='Товар'
        verbose_name_plural = 'Товары'