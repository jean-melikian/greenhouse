from rest_framework import serializers

from .models import SensorsEntry


class SensorsEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = SensorsEntry
		fields = ('id', 'entry_date', 'entry_hydro', 'entry_temperature')
