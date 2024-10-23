from django.utils import timezone

from rest_framework import generics, status
from rest_framework.response import Response

from .permission import HasValidTokenPermission
from .serializers import (TelegramUserSerializer,
                          ReminderSerializer,
                          NotificationSerializer,
                          CreateReminderSerializer)
from .models import TelegramUser, Reminder, Notification


class TelegramUserCreateView(generics.CreateAPIView):
    """Создание пользователя"""
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    authentication_classes = []
    permission_classes = [HasValidTokenPermission]


class TelegramUserInfoView(generics.RetrieveUpdateAPIView):
    """Получение/изменение информации о пользователе"""
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    lookup_field = 'telegram_id'
    authentication_classes = []
    permission_classes = [HasValidTokenPermission]


class TelegramUserInfoByUsernameView(generics.RetrieveUpdateAPIView):
    """Получение/изменение информации о пользователе по username"""
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    lookup_field = 'username'
    authentication_classes = []
    permission_classes = [HasValidTokenPermission]


class CurrentNotificationsView(generics.ListAPIView):
    """Список актуальных на данный момент уведомлений"""
    serializer_class = NotificationSerializer
    authentication_classes = []
    permission_classes = [HasValidTokenPermission]

    def get_queryset(self):
        now = timezone.localtime(timezone.now()).replace(second=0, microsecond=0)
        notifications = Notification.objects.filter(time=now.time())

        notifications = notifications.exclude(
            user__vacation__start_date__lte=now.date(),
            user__vacation__end_date__gte=now.date()
        ).distinct()

        return notifications

class ReminderView(generics.GenericAPIView):
    """Создание и просмотр напоминаний"""
    authentication_classes = []
    permission_classes = [HasValidTokenPermission]

    def get(self, request, *args, **kwargs):
        now = timezone.localtime(timezone.now())
        reminders = Reminder.objects.filter(time__lte=now)
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CreateReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRemindersDestroyView(generics.DestroyAPIView):
    """Удаление всех напоминаний для пользователя"""
    authentication_classes = []
    permission_classes = [HasValidTokenPermission]

    def delete(self, request, *args, **kwargs):
        telegram_id = kwargs.get('telegram_id')

        reminders = Reminder.objects.filter(user__telegram_id=telegram_id)
        reminders.delete()

        return Response({'message': 'All reminders deleted for user'},
                        status=status.HTTP_204_NO_CONTENT)

