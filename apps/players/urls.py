from django.urls import path

from apps.players.views import PlayerDetailView


urlpatterns = [
    path('<str:nickname>/<int:pk>/', PlayerDetailView.as_view()),
]
