from rest_framework import serializers
from .models import TelegramUser, Vacation, Reminder, Notification


class ReminderSerializer(serializers.ModelSerializer):
    telegram_id = serializers.SerializerMethodField()

    class Meta:
        model = Reminder
        fields = ['telegram_id', 'id', 'type', 'time']

    def get_telegram_id(self, obj):
        return obj.user.telegram_id


class CreateReminderSerializer(serializers.ModelSerializer):
    telegram_id = serializers.CharField(write_only=True)

    class Meta:
        model = Reminder
        fields = ['telegram_id', 'type', 'time']

    def create(self, validated_data):
        telegram_id = validated_data.pop('telegram_id')
        user = TelegramUser.objects.get(telegram_id=telegram_id)
        return Reminder.objects.create(user=user, **validated_data)


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ['start_date', 'end_date']


class NotificationSerializer(serializers.ModelSerializer):
    telegram_id = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['telegram_id', 'type', 'time']

    def get_telegram_id(self, obj):
        return obj.user.telegram_id


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['telegram_id', 'username']
