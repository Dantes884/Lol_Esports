from django.db import models

from apps.players.models import Player


class Team(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField()
    region = models.CharField(max_length=25)
    active_players = models.ManyToManyField(Player, related_name='team')
    substitution = models.ManyToManyField(Player, related_name='sub', null=True, blank=True)

    @property
    def sorted_active_players(self):
        sorted_players_list = sorted(self.active_players.all(), key=lambda player: player.role)
        active_players_info = []

        for player in sorted_players_list:
            if player.role != 6:
                player_info = (
                    f'Nationality: {player.nation}, '
                    f'Nickname: {player.nickname}, '
                    f'Photo: http://127.0.0.1:8000/{player.photo.url}, '
                    f'Role: {player.get_role_display()}'
                )
                active_players_info.append(player_info)

        return '\n'.join(active_players_info)

    @property
    def head_couch(self):
        sorted_coach_list = sorted(self.active_players.all(), key=lambda player: player.role)
        active_coach_info = []

        for player in sorted_coach_list:
            if player.role == 6:
                player_info = (
                    f'Nationality: {player.nation}, '
                    f'Nickname: {player.nickname}, '
                )
                active_coach_info.append(player_info)

        return '\n'.join(active_coach_info)

    @property
    def sorted_sub_players(self):
        sorted_players_list = sorted(self.substitution.all(), key=lambda player: player.role)
        player_info = [(f'Nationality: {player.nation}, '
                        f'Nickname: {player.nickname}, '
                        f'Role: Sub/{player.get_role_display()}') for player in sorted_players_list]
        return '\n'.join(player_info)

    @property
    def trophies(self):
        trophy_list = [f'Trophy: http://127.0.0.1:8000/{trophy.trophy.url}, Event: {trophy.title}' for trophy in self.trophy.all()]
        if trophy_list:
            return '\n'.join(trophy_list)
        return 'Empty'

    def __str__(self):
        return self.name
