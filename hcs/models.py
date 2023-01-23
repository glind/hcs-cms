from django.db import models
from datetime import timedelta
from decimal import Decimal
import uuid

from django.conf import settings

from django.contrib import admin
from django.utils import timezone
from django.contrib.auth import get_user_model

from modelcluster.fields import ParentalKey

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class ContactMail(models.Model):
    name = models.CharField(max_length=255, blank=True)
    inquiry = models.CharField(max_length=255, blank=True)
    message = models.TextField(blank=True)
    email = models.CharField(max_length=255, blank=True)
    file = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def clean_email(self):
        original_email = self.cleaned_data.get('email')

        if "@" not in original_email:
            raise ValidationError("Invalid Email address")

        if "." not in original_email:
            raise ValidationError("Invalid Email address")

        return original_email

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(ContactMail, self).save(*args, **kwargs)


class ContactMailAdmin(admin.ModelAdmin):
    list_display = ('name','email','url','create_date','edit_date')
    search_fields = ('name','email')
    list_filter = ('name',)
    display = 'Contact Form'


class Entry(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(null=True, blank=True)
    entry_type = models.CharField(max_length=255, null=True, blank=True)
    entry_catagory = models.CharField(max_length=255, null=True, blank=True)
    entry_url = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(Entry, self).save(*args, **kwargs)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('name','entry_type','create_date','edit_date')
    search_fields = ('name','email')
    list_filter = ('name',)
    display = 'Entry Form'


class Hack(models.Model):
    entry = models.ForeignKey(Entry, models.SET_NULL, null=True, blank=True)
    entry_type = models.CharField(max_length=255, null=True, blank=True)
    entry_catagory = models.CharField(max_length=255, null=True, blank=True)
    votes = models.IntegerField(default=0)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    @admin.display(description='Entry', ordering='entry__name')
    def get_entry_name(self, obj):
        return obj.entry.name

    def __unicode__(self):
        return self.entry__name

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(Hack, self).save(*args, **kwargs)


class HackAdmin(admin.ModelAdmin):
    list_display = ('entry','votes','create_date','edit_date')
    search_fields = ('entry_type','entry')
    list_filter = ('entry',)
    display = 'Hack Form'


class Crack(models.Model):
    entry = models.ForeignKey(Entry, models.SET_NULL, null=True, blank=True)
    entry_type = models.CharField(max_length=255, null=True, blank=True)
    entry_catagory = models.CharField(max_length=255, null=True, blank=True)
    votes = models.IntegerField(default=0)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    @admin.display(description='Entry', ordering='entry__name')
    def get_entry_name(self, obj):
        return obj.entry.name

    def __unicode__(self):
        return self.entry__name

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(Hack, self).save(*args, **kwargs)


class CrackAdmin(admin.ModelAdmin):
    list_display = ('entry','votes','create_date','edit_date')
    search_fields = ('entry_type','entry')
    list_filter = ('entry',)
    display = 'Crack Form'


class Scam(models.Model):
    entry = models.ForeignKey(Entry, models.SET_NULL, null=True, blank=True)
    entry_type = models.CharField(max_length=255, null=True, blank=True)
    entry_catagory = models.CharField(max_length=255, null=True, blank=True)
    votes = models.IntegerField(default=0)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    @admin.display(description='Entry', ordering='entry__name')
    def get_entry_name(self, obj):
        return obj.entry.name

    def __unicode__(self):
        return self.entry__name

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(Scam, self).save(*args, **kwargs)


class ScamAdmin(admin.ModelAdmin):
    list_display = ('entry','votes','create_date','edit_date')
    search_fields = ('entry_type','entry')
    list_filter = ('entry',)
    display = 'Scam Form'


class UserVote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET(get_sentinel_user),)
    entry = models.ForeignKey(Entry, models.SET_NULL, null=True, blank=True)
    vote = models.CharField(max_length=255, null=True, blank=True)
    hack = models.ForeignKey(Hack, models.SET_NULL, null=True, blank=True)
    crack = models.ForeignKey(Crack, models.SET_NULL, null=True, blank=True)
    scam = models.ForeignKey(Scam, models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.user__name

    def save(self, *args, **kwargs):
        # onsave add create date or update edit date
        if self.create_date == None:
            self.create_date = timezone.now()
        self.edit_date = timezone.now()
        super(UserVote, self).save(*args, **kwargs)


class UserVoteAdmin(admin.ModelAdmin):
    list_display = ('user','entry','hack','crack','scam','create_date','edit_date')
    search_fields = ('user','entry')
    list_filter = ('user',)
    display = 'Entry Form'


