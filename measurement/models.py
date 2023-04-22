from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    description = models.CharField(max_length=50, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Датчик', related_name='measurements')
    temp = models.FloatField(null=False, verbose_name='Температура')
    dt = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'