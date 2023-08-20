from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = 'id name icon sorted_active_players'.split()


class TeamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = 'name region icon sorted_active_players head_couch trophies sorted_sub_players'.split()
