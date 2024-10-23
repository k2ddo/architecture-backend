from django.urls import path
from .views import (TelegramUserCreateView,
                    TelegramUserInfoView,
                    TelegramUserInfoByUsernameView,
                    ReminderView,
                    CurrentNotificationsView,
                    UserRemindersDestroyView)

urlpatterns = [
    path('users/', TelegramUserCreateView.as_view()),
    path('users/<int:telegram_id>/', TelegramUserInfoView.as_view()),
    path('users/<str:username>/', TelegramUserInfoByUsernameView.as_view()),

    path('reminders/', ReminderView.as_view()),
    path('reminders/delete/<int:telegram_id>/', UserRemindersDestroyView.as_view()),

    path('notifications/', CurrentNotificationsView.as_view())
]
