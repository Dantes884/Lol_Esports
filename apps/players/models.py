from django.db import models


class Player(models.Model):
    CHOICE_POSITION = (
        (1, 'Top Laner'),
        (2, 'Jungler'),
        (3, 'Mid Laner'),
        (4, 'Bot Laner'),
        (5, 'Support'),
        (6, 'Coach'),
    )

    name = models.CharField(max_length=60)
    nickname = models.CharField(max_length=50)
    photo = models.ImageField()
    age = models.PositiveIntegerField(blank=True)
    nation = models.CharField(max_length=30)
    role = models.IntegerField(choices=CHOICE_POSITION, max_length=20)
    retired = models.BooleanField()

    @property
    def current_team(self):
        current_team = [f'Icon: {team.icon.url}, Title: {team.name}' for team in self.team.all()]
        return '\n'.join(current_team)

    def __str__(self):
        return self.nickname
