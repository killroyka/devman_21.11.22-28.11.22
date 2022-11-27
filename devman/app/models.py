from django.db import models
from django.urls import reverse


class GeoJSON(models.Model):
    title = models.CharField(max_length=60, verbose_name='Оглавление')
    place_id = models.CharField(max_length=60, unique=True, verbose_name='идентификатор локации', blank=True, null=True)
    description_short = models.CharField(max_length=255, verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    lng = models.DecimalField(max_digits=16, decimal_places=14, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=16, decimal_places=14, verbose_name='Широта')

    def get_json_data_url(self):
        print(reverse("GeoJSONDetail", args=[str(self.id)]))
        return reverse("GeoJSONDetail", args=[str(self.id)])

    class Meta:
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __str__(self):
        return self.title


class GeoImage(models.Model):
    img = models.ImageField("Картинка точки")
    index = models.IntegerField("порядок изображения",
                                help_text="Введите число кикм по порядку должно быть изображение",
                                blank=True,
                                null=True,
                                unique=True)
    geojson = models.ForeignKey(GeoJSON,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True,
                                related_name='images')

    class Meta:
        verbose_name = 'Картинка локации'
        verbose_name_plural = 'Картинки локации'
