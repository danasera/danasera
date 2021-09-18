

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# статусы: (открытый, закрытый, черновик)
STATUS_CHOICES = (
    ('open', 'Открытое'),
    ('closed', 'Закрытое'),
    ('draft', 'Черновик')
)



class Category(models.Model):
    name = models.CharField('Name', max_length=60)
    slug = models.SlugField(primary_key=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def str(self):
        return self.name


class Product(models.Model):
    title = models.CharField('Title', max_length=55)
    description = models.TextField('Description')
    price = models.DecimalField('Price', max_digits=100, decimal_places=3)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='cate', verbose_name='Категория')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def str(self):
        return self.title


