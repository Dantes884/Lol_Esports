from django.db import models

from apps.teams.models import Team


class Event(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField()
    date = models.DateField()
    end_date = models.DateField()
    prize_pool = models.PositiveIntegerField()
    trophy = models.ImageField()
    location = models.CharField(max_length=60, blank=True, default='online')
    teams = models.ManyToManyField(Team, related_name='event')
    winner = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='trophy', null=True, blank=True,
                               default=None)

    @property
    def count_teams(self):
        return self.teams.count()

    @property
    def prize_distribution(self):
        first_place_prize = self.prize_pool * 0.5
        second_place_prize = self.prize_pool * 0.3
        third_place_prize = self.prize_pool * 0.2

        return {
            "1st Place": f"${first_place_prize}",
            "2nd Place": f"${second_place_prize}",
            "3rd Place": f"${third_place_prize}"
        }

    @property
    def date_time(self):
        return f'{self.date} - {self.end_date}'

    def __str__(self):
        return self.title
