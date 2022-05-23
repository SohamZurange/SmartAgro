from django.contrib import admin

from .models import Auction, Bid
from .models import Contact

admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Contact)
