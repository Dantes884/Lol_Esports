from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.teams.models import Team
from apps.teams.serializers import TeamSerializer, TeamDetailSerializer


class TeamListView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [AllowAny]


class TeamDetailView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer
    permission_classes = [AllowAny]
