# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class AccountEmailaddress(models.Model):
#     email = models.CharField(unique=True, max_length=254)
#     verified = models.IntegerField()
#     primary = models.IntegerField()
#     user = models.ForeignKey('UsersUser', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'account_emailaddress'
#
#
# class AccountEmailconfirmation(models.Model):
#     created = models.DateTimeField()
#     sent = models.DateTimeField(blank=True, null=True)
#     key = models.CharField(unique=True, max_length=64)
#     email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'account_emailconfirmation'
#
#
# class AlbumTracks(models.Model):
#     albumid = models.CharField(db_column='albumId', primary_key=True, max_length=255)  # Field name made lowercase.
#     trackid = models.CharField(db_column='trackId', max_length=255)  # Field name made lowercase.
#     trackname = models.CharField(db_column='trackName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'album_tracks'
#         unique_together = (('albumid', 'trackid'),)
#
#
# class ArtistAlbums(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
#     albumid = models.CharField(db_column='albumId', max_length=255)  # Field name made lowercase.
#     albumname = models.CharField(db_column='albumName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     albumtype = models.CharField(db_column='albumType', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     imageurl = models.CharField(db_column='imageUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     releasedate = models.DateTimeField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
#     releasedateprecision = models.CharField(db_column='releaseDatePrecision', max_length=50, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'artist_albums'
#         unique_together = (('artistid', 'albumid'),)
#
#
# class ArtistFeatures(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
#     tempo = models.FloatField(blank=True, null=True)
#     energy = models.FloatField(blank=True, null=True)
#     speechiness = models.FloatField(blank=True, null=True)
#     instrumentalness = models.FloatField(blank=True, null=True)
#     duration_ms = models.FloatField(blank=True, null=True)
#     liveness = models.FloatField(blank=True, null=True)
#     acousticness = models.FloatField(blank=True, null=True)
#     loudness = models.FloatField(blank=True, null=True)
#     valence = models.FloatField(blank=True, null=True)
#     danceability = models.FloatField(blank=True, null=True)
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'artist_features'
#
#
# class ArtistGenres(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=50)  # Field name made lowercase.
#     genre = models.CharField(max_length=50)
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'artist_genres'
#         unique_together = (('artistid', 'genre'),)
#
#
# class Artists(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=255)  # Field name made lowercase.
#     artistname = models.CharField(db_column='artistName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     attractionid = models.CharField(db_column='attractionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     popularity = models.IntegerField(blank=True, null=True)
#     followers = models.IntegerField(blank=True, null=True)
#     externalurl = models.CharField(db_column='externalUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#     imageurl = models.CharField(db_column='imageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'artists'
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class DeleteAlbums(models.Model):
#     albumid = models.CharField(db_column='albumId', primary_key=True, max_length=255)  # Field name made lowercase.
#     reason = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'delete_albums'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey('UsersUser', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class DjangoSite(models.Model):
#     domain = models.CharField(unique=True, max_length=100)
#     name = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'django_site'
#
#
# class EventArtists(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     artistid = models.CharField(db_column='artistId', max_length=255)  # Field name made lowercase.
#     artistname = models.CharField(db_column='artistName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     attractionid = models.CharField(db_column='attractionId', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'event_artists'
#         unique_together = (('eventid', 'artistid'),)
#
#
# class EventAttractions(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     attractionid = models.CharField(db_column='attractionId', max_length=255)  # Field name made lowercase.
#     attractionimageurl = models.CharField(db_column='attractionImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     attractionname = models.CharField(db_column='attractionName', max_length=255)  # Field name made lowercase.
#     attractionurl = models.CharField(db_column='attractionUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'event_attractions'
#         unique_together = (('eventid', 'attractionid'),)
#
#
# class EventClassifications(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     classificationsegment = models.CharField(db_column='classificationSegment', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classificationgenre = models.CharField(db_column='classificationGenre', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classificationsubgenre = models.CharField(db_column='classificationSubGenre', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classificationsubtype = models.CharField(db_column='classificationSubType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     classificationtype = models.CharField(db_column='classificationType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'event_classifications'
#
#
# class EventVenues(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     venueid = models.CharField(db_column='venueId', max_length=255)  # Field name made lowercase.
#     venuename = models.CharField(db_column='venueName', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     venuecity = models.CharField(db_column='venueCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuestatecode = models.CharField(db_column='venueStateCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     venuecountrycode = models.CharField(db_column='venueCountryCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     venuestreet = models.CharField(db_column='venueStreet', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     venuezipcode = models.CharField(db_column='venueZipCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     venuelatitude = models.FloatField(db_column='venueLatitude', blank=True, null=True)  # Field name made lowercase.
#     venuelongitude = models.FloatField(db_column='venueLongitude', blank=True, null=True)  # Field name made lowercase.
#     venueurl = models.CharField(db_column='venueUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     venuetimezone = models.CharField(db_column='venueTimezone', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'event_venues'
#         unique_together = (('eventid', 'venueid'),)
#
#
# class Events(models.Model):
#     eventid = models.CharField(db_column='eventId', primary_key=True, max_length=255)  # Field name made lowercase.
#     eventimageurl = models.CharField(db_column='eventImageUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     eventname = models.CharField(db_column='eventName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     eventstartlocaldate = models.DateField(db_column='eventStartLocalDate', blank=True, null=True)  # Field name made lowercase.
#     eventstatus = models.CharField(db_column='eventStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     onsaleenddatetime = models.DateTimeField(db_column='onsaleEndDateTime', blank=True, null=True)  # Field name made lowercase.
#     onsalestartdatetime = models.DateTimeField(db_column='onsaleStartDateTime', blank=True, null=True)  # Field name made lowercase.
#     primaryeventurl = models.CharField(db_column='primaryEventUrl', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     source = models.CharField(max_length=50, blank=True, null=True)
#     currency = models.CharField(max_length=50, blank=True, null=True)
#     maxprice = models.FloatField(db_column='maxPrice', blank=True, null=True)  # Field name made lowercase.
#     minprice = models.FloatField(db_column='minPrice', blank=True, null=True)  # Field name made lowercase.
#     eventstartlocaltime = models.TimeField(db_column='eventStartLocalTime', blank=True, null=True)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'events'
#
#
# class FeatureMetrics(models.Model):
#     feature = models.CharField(primary_key=True, max_length=50)
#     mean = models.FloatField(blank=True, null=True)
#     std = models.FloatField(blank=True, null=True)
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'feature_metrics'
#
#
# class RelatedArtists(models.Model):
#     artistid = models.CharField(db_column='artistId', primary_key=True, max_length=50)  # Field name made lowercase.
#     relatedartistid = models.CharField(db_column='relatedArtistId', max_length=50)  # Field name made lowercase.
#     updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'related_artists'
#         unique_together = (('artistid', 'relatedartistid'),)
#
#
# class SocialaccountSocialaccount(models.Model):
#     provider = models.CharField(max_length=30)
#     uid = models.CharField(max_length=191)
#     last_login = models.DateTimeField()
#     date_joined = models.DateTimeField()
#     extra_data = models.TextField()
#     user = models.ForeignKey('UsersUser', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'socialaccount_socialaccount'
#         unique_together = (('provider', 'uid'),)
#
#
# class SocialaccountSocialapp(models.Model):
#     provider = models.CharField(max_length=30)
#     name = models.CharField(max_length=40)
#     client_id = models.CharField(max_length=191)
#     secret = models.CharField(max_length=191)
#     key = models.CharField(max_length=191)
#
#     class Meta:
#         managed = False
#         db_table = 'socialaccount_socialapp'
#
#
# class SocialaccountSocialappSites(models.Model):
#     socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
#     site = models.ForeignKey(DjangoSite, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'socialaccount_socialapp_sites'
#         unique_together = (('socialapp', 'site'),)
#
#
# class SocialaccountSocialtoken(models.Model):
#     token = models.TextField()
#     token_secret = models.TextField()
#     expires_at = models.DateTimeField(blank=True, null=True)
#     account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
#     app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'socialaccount_socialtoken'
#         unique_together = (('app', 'account'),)
#
#
# class UsersUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#     name = models.CharField(max_length=255)
#     bio = models.TextField(blank=True, null=True)
#     gender = models.CharField(max_length=80, blank=True, null=True)
#     phone = models.CharField(max_length=140, blank=True, null=True)
#     website = models.CharField(max_length=200, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'users_user'
#
#
# class UsersUserGroups(models.Model):
#     user = models.ForeignKey(UsersUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'users_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class UsersUserUserPermissions(models.Model):
#     user = models.ForeignKey(UsersUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'users_user_user_permissions'
#         unique_together = (('user', 'permission'),)
