from django.db import models


class GeoJSON(models.Model):
    title = models.CharField(max_length=60, verbose_name='Оглавление')
    description_short = models.CharField(max_length=255, verbose_name='Короткое описание')
    description_long = models.TextField(verbose_name='Длинное описание')
    lng = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='Широта')

    class Meta:
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __str__(self):
        return self.title


class GeoImage(models.Model):
    img = models.ImageField("Картинка точки", upload_to="GeoImages/")
    index = models.IntegerField("порядок изображения",
                                help_text="Введите число кикм по порядку должно быть изображение",
                                blank=True,
                                null=True,
                                unique=True)
    geojson = models.ForeignKey(GeoJSON, on_delete=models.CASCADE, null=True, blank=True, related_name='images')

    class Meta:
        verbose_name = 'Картинка локации'
        verbose_name_plural = 'Картинки локации'
