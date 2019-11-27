from django.db import models

# Create your models here.
class Client(models.Model):
    site_name = models.CharField('Web site', max_length=50)
    client_name = models.CharField('Имя Клиента', max_length=50)
    description = models.TextField('Описание', max_length=50)
    phone = models.CharField('Контакты', max_length=50)
    price = models.CharField('Цена', max_length=50)
    date = models.DateField('Абонплата', max_length=50)

    #class Meta:
    #    verbose_name = '[Список клиентов] Client'

    def str(self):
        return self.site_name

