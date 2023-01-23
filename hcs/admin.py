from .models import *
from django.contrib import admin

admin.site.register(ContactMail, ContactMailAdmin)
admin.site.register(Hack, HackAdmin)
admin.site.register(Crack, CrackAdmin)
admin.site.register(Scam, ScamAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(UserVote, UserVoteAdmin)
