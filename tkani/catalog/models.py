from django.db import models
from django.contrib.auth import get_user_model

MAX_CHAR = 256
User = get_user_model()


class Category(models.Model):

    title = models.CharField(max_length=MAX_CHAR, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField('Фото', upload_to='category_images', blank=True)
    slug = models.SlugField(unique=True, verbose_name='Идентификатор',
                            help_text='Идентификатор страницы для URL; '
                            'разрешены символы латиницы, цифры, дефис и '
                            'подчёркивание.')

    class Meta:
        """Класс meta."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Метод str."""
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=MAX_CHAR, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField('Фото', upload_to='category_images', blank=True)
    slug = models.SlugField(unique=True, verbose_name='Идентификатор',
                            help_text='Идентификатор страницы для URL; '
                            'разрешены символы латиницы, цифры, дефис и '
                            'подчёркивание.')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='категория'
    )

    class Meta:
        """Класс meta."""

        verbose_name = 'субкатегория'
        verbose_name_plural = 'Субатегории'

    def __str__(self):
        """Метод str."""
        return self.title

class Item(models.Model):
    """Модель поста."""

    title = models.CharField(max_length=MAX_CHAR, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10) 
    price_opt = models.DecimalField(max_digits=5, decimal_places=2, default=10) 
    item_width = models.TextField(verbose_name='Ширина полотна', default='10')
    sku = models.TextField(verbose_name='Артикул', default='10')
    density = models.TextField(verbose_name='Плотность', default='10')
    type_fabric = models.TextField(verbose_name='Тип ткани', default='10')
    made_in = models.TextField(verbose_name='Страна производитель', default='10')
    color = models.TextField(verbose_name='Цвет', default='10')
    image = models.ImageField('Фото', upload_to='category_images', blank=True)
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.')
    is_new = models.BooleanField(
        default=False,
        verbose_name='Новинка')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория'
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Субкатегория'
    )

    class Meta:
        """Класс meta."""

        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
