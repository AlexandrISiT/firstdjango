from django.db import models

# Create your models here.

class Items(models.Model):
    title = models.CharField('Название', max_length=50)
    quantity = models.IntegerField('Количество', max_length=6)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'