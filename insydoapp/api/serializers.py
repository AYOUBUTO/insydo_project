__author__ = 'Apolikamixitos'
from rest_framework import serializers


class LongestStringInputSerializer(serializers.Serializer):
    list_strings = serializers.ListField(
        child=serializers.CharField(required=True, allow_blank=True, max_length=100)
    )