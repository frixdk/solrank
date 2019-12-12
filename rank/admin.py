from django.contrib import admin

# Register your models here.
from .models import Player
admin.site.register(Player)

from .models import Deck
admin.site.register(Deck)

from .models import DeckPlayer
admin.site.register(DeckPlayer)

from .models import Match
admin.site.register(Match)