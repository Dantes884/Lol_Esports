from django.urls import path

from apps.competitives.views import EventListView, EventDetailView


urlpatterns = [
    path('', EventListView.as_view()),
    path('<int:pk>/', EventDetailView.as_view()),
]
