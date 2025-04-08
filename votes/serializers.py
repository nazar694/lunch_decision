from django.utils import timezone

from rest_framework import serializers
from .models import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'employee', 'restaurant', 'day']
        read_only_fields = ['employee', 'day']

    def validate(self, attrs):
        user = self.context['request'].user
        today = timezone.now().weekday()
        if Vote.objects.filter(employee=user, day=today).exists():
            raise serializers.ValidationError("The fields employee, day must make a unique set.")
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        validated_data['employee'] = request.user
        validated_data['day'] = timezone.now().weekday()
        return super().create(validated_data)
