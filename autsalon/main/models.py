from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brend nomi")
    country = models.CharField(max_length=100, verbose_name="Kelib chiqishi")
    founded_at = models.DateTimeField(null=True, blank=True, verbose_name="Tashkil topgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Brendlar"
        verbose_name = "Brend"


class Car(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mashina nomi")
    photo = models.ImageField(upload_to="new/photos/", null=True, blank=True)
    model_year = models.IntegerField(verbose_name="Model yili")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name="Brendi")

    def __str__(self):
        return f"{self.name} ({self.model_year})"

    class Meta:
        verbose_name_plural = "Mashinalar"
        verbose_name = "Mashina"
