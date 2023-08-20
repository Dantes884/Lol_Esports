from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Player
from .serializers import PlayerSerializer


class PlayerDetailView(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        queryset = self.get_queryset()
        nickname = self.kwargs['nickname']
        pk = self.kwargs['pk']
        player = queryset.filter(nickname=nickname, pk=pk).first()
        return player
