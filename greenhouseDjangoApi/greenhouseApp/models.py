from django.db import models
from datetime import timedelta
from django.utils import timezone
import datetime


# Create your models here.

def get_expiration_date():
	return timezone.now() + timedelta(days=1)


class Token(models.Model):
	user = models.OneToOneField('auth.User', on_delete=models.CASCADE, unique=True)
	hash = models.CharField(max_length=255)
	expiration_date = models.DateTimeField(default=get_expiration_date())

	def is_expired(self):
		return self.expiration_date < timezone.now()


class SensorsEntry(models.Model):
	entry_date = models.DateTimeField(auto_now_add=True, blank=True)
	entry_hydro = models.IntegerField(default=0)
	entry_temperature = models.IntegerField(default=0)

	def __str__(self):
		return "(" + self.entry_date.strftime('%d/%m/%Y') + ") :\n(Hydro: " + str(
			self.entry_hydro) + ",  Temperature : " + str(
			self.entry_temperature) + ")";


class Meta:
	ordering = ('entry_date',)
