from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.name


class Deck(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class DeckPlayer(models.Model):
    player = models.ForeignKey(Player, blank=False, null=False, related_name="player", on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, blank=False, null=False, related_name="deck", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.player} - {self.deck}'


class Match(models.Model):
    deck_players = models.ManyToManyField(DeckPlayer, related_name="deck_players")
    winner = models.ForeignKey(DeckPlayer, blank=False, null=False, related_name="winner", on_delete=models.CASCADE)

    def __str__(self):  
        return f'{self.deck_players}. Winner: {self.winner}'