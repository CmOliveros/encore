from rest_framework import serializers
from.models import MasterUser, TalentUser, VenueUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterUser
        fields = ('id', 'first_name', 'last_name', 'birth_date',
                  'city', 'state', 'country', 'friends')


class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentUser
        fields = ('id', 'name', 'members', 'discography',
                  'city', 'state', 'country', 'fans', 'genres')


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueUser
        fields = ('id', 'name', 'city', 'state', 'country', 'events', 'fans')
