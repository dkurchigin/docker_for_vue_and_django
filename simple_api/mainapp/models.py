from django.db import models

class POI(models.Model):
    class Meta:
        verbose_name = 'Содержимое POI'
        verbose_name_plural = 'Содержимое POI'

    poi_info = models.TextField(verbose_name='Информация', default='', blank=True, null=True)

    def __str__(self):
        return f'{self.pk} - {self.poi_info}'

