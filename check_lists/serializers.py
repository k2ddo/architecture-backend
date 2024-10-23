from rest_framework import serializers

from .models import CheckList


class CheckListNamesSerializer(serializers.ModelSerializer):
    """Сериализатор названий чек-листов"""
    class Meta:
        model = CheckList
        fields = ('id', 'name',)
