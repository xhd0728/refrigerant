from rest_framework import serializers
from .models import Refrigerant


class RefrigerantSerializer(serializers.ModelSerializer):
    rid = serializers.SerializerMethodField()

    class Meta:
        model = Refrigerant
        fields = (
            'rid', 'code', 'formula', 'molecular_weight', 'curve_data', 'type', 'safety_index', 'env_impact_index'
        )

    def get_rid(self, obj):
        return obj.id
