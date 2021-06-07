from django.db import models


# Main user model
class MasterUser(models.Model):
    city = models.CharField(blank=False, null=True, max_length=30)
    state = models.CharField(blank=True, null=True, max_length=30)
    country = models.CharField(blank=False, null=True, max_length=30)
    user_network = models.ManyToManyField('MasterUser', editable=False)
    posts = models.ManyToManyField('Post', editable=False)
    image = models.FileField(upload_to='images/', blank=True, null=True)


# General site user (Can belong to talent, venue, or other groups)
class PersonUser(MasterUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Musical act.  Solo or group
class TalentUser(MasterUser):
    name = models.CharField(max_length=30)

    # List of dicts - Member names, roles, DB ID if available
    members = models.JSONField(blank=True, null=False,
                               editable=False, default=list)

    # API contacts for music apps
    apple_music_id = models.CharField(blank=True, null=False,
                                      max_length=100)

    spotify_id = models.CharField(blank=True, null=False,
                                  max_length=100)

    # Genres - Reference "./genres.json"
    genres = models.JSONField(blank=True, null=False,
                              editable=False, default=list)

    def __str__(self):
        return f'{self.name}'


class VenueUser(MasterUser):
    name = models.CharField(max_length=30)
    street_address = models.CharField(max_length=100)
    zip_code = models.CharField(blank=True, null=False, max_length=100)

    lat = models.CharField(max_length=30, blank=True, null=True,
                           editable=False)

    long = models.CharField(max_length=30, blank=True, null=True,
                            editable=False)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    creator = models.ForeignKey(MasterUser, on_delete=models.CASCADE)
    date_created = models.DateField()
    content = models.CharField(max_length=500, blank=False, null=False)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.date_created} - {self.creator_id}'


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date = models.DateField()
    attendees = models.ManyToManyField(PersonUser)
    venue = models.ForeignKey(VenueUser, on_delete=models.CASCADE)

    talent = models.JSONField(blank=True, null=False,
                              editable=False, default=list)
