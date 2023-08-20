from django.urls import path

from apps.teams.views import TeamListView, TeamDetailView


urlpatterns = [
    path('', TeamListView.as_view()),
    path('<int:pk>/', TeamDetailView.as_view()),
]
