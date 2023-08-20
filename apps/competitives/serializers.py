from rest_framework import serializers

from apps.competitives.models import Event
from apps.teams.serializers import TeamSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = 'banner title date_time'.split()


class EventDetailSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)

    class Meta:
        model = Event
        fields = 'banner title date_time count_teams location prize_pool prize_distribution teams'.split()
