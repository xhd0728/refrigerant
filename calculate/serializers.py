from rest_framework import serializers

from .models import Record


class CalculateRecordSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d, %H:%M:%S")
    rid = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = (
            'id', 'create_time', 'data'
        )

    def get_rid(self, obj):
        return obj.id
