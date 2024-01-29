from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from tinymce.models import HTMLField



# Create your models here.

class Uzduotis(models.Model):
    data = models.DateTimeField("Data", default=timezone.datetime.now)
    uzduoties_tekstas = HTMLField(verbose_name="Užduotis")
    vartotojas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.data} {self.vartotojas}"

    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('uzduotis_detail', args=[str(self.id)])


