from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.competitives.models import Event
from apps.competitives.serializers import EventSerializer, EventDetailSerializer


class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    permission_classes = [AllowAny]
