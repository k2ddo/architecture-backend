from django.urls import path

from .views import CheckListNamesView, CheckListQuestionsView


urlpatterns = [
    path('', CheckListNamesView.as_view()),
    path('<int:pk>/', CheckListQuestionsView.as_view())
]
