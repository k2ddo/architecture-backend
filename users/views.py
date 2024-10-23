from datetime import timedelta

from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()

    def list(self, request, *args, **kwargs):
        user = request.user
        today = timezone.localtime(timezone.now())
        tomorrow = today + timedelta(days=1)

        tasks_for_today = Task.objects.filter(user=user, due_date=today.date())
        tasks_for_tomorrow = Task.objects.filter(user=user, due_date=tomorrow.date())

        serializer_today = TaskSerializer(tasks_for_today, many=True)
        serializer_tomorrow = TaskSerializer(tasks_for_tomorrow, many=True)

        return Response({
            'today': serializer_today.data,
            'tomorrow': serializer_tomorrow.data
        }, status=status.HTTP_200_OK)
