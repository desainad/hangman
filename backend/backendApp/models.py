from django.db import models

# Create your models here.

class s_country(models.Model):
    cntry_name = models.CharField(max_length=80)
    cntry_iso = models.CharField(max_length=2, blank=True, null=True)
    cntry_language = models.CharField(max_length=80, blank=True, null=True)
    cntry_nickname = models.CharField(max_length=80, blank=True, null=True)
    cntry_iso3 = models.CharField(max_length=3, blank=True, null=True)
    cntry_numcode = models.IntegerField(blank=True, null=True)
    cntry_phonecode = models.IntegerField(blank=True, null=True)
    cntry_capital = models.CharField(max_length=100, blank=True, null=True)
    cntry_currency = models.CharField(max_length=80, blank=True, null=True)
    def __str__(self):
        return (self.cntry_name)

class s_language(models.Model):
    lngg_code = models.CharField(max_length=5)
    lngg_name = models.CharField(max_length=80)

    def __str__(self):
        return [self.lngg_name]

class s_profession(models.Model):
    profession_name = models.CharField(max_length=80)

    def __str__(self):
        return (self.profession_name)

class s_genre(models.Model):
    GENRE_CHOICES=[("M", "Movies"),("T","Tracks")]
    genre_type = models.CharField(max_length=50)
    genre_for = models.CharField(max_length=1, choices=GENRE_CHOICES, blank=True, null=True)

    def __str__(self):
        return (self.genre_type)

class s_artist(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female")]
    artist_full_name = models.CharField(max_length=50)
    artist_title = models.CharField(max_length=15, blank=True, null=True)
    artist_first_name = models.CharField(max_length=50, blank=True, null=True)
    artist_middle_name = models.CharField(max_length=50, blank=True, null=True)
    artist_last_name = models.CharField(max_length=50, blank=True, null=True)
    artist_suffix = models.CharField(max_length=50, blank=True, null=True)
    artist_nickname = models.CharField(max_length=50, blank=True, null=True)
    artist_surname = models.CharField(max_length=50, blank=True, null=True)
    artist_initials = models.CharField(
        max_length=1, blank=True, null=True)
    artist_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    artist_citizenof = models.ForeignKey(s_country, blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return (self.artist_full_name)

class s_movie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_genre = models.ForeignKey(
        s_genre, blank=True, null=True, on_delete=models.DO_NOTHING)
    movie_based = models.CharField(max_length=100, null=True, blank = True)
    movie_released = models.CharField(max_length=30, blank=True, null=True)
    movie_language = models.CharField(
        max_length=100, default='Hindi', blank=True, null=True)
    movie_country = models.ForeignKey(
        s_country, blank=True, null=True, on_delete=models.DO_NOTHING)
    movie_duration = models.CharField(
        max_length=15, blank=True, null=True)
    movie_budget = models.CharField(
        max_length=30, blank=True, null=True)
    movie_boxoffice = models.CharField(
        max_length=30, blank=True, null=True)
    movie_plot = models.TextField(blank=True, null=True)
    movie_achievements = models.TextField(blank=True, null=True)

    def __str__(self):
        return (self.movie_title)

class s_company(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return (self.company_name)

class s_track(models.Model):
    track_title = models.CharField(max_length=100)
    movie = models.ForeignKey(s_movie, blank=True, null=True, on_delete=models.DO_NOTHING)
    track_lyrics: models.TextField(max_length=300)

    def __str__(self):
        return [self.track_title]

# Intersection tables

class s_mv_artst_prfssn(models.Model):
    movie = models.ForeignKey(
        s_movie, blank=True, null=True, on_delete=models.DO_NOTHING)
    artist = models.ForeignKey(
        s_artist, blank=True, null=True, on_delete=models.DO_NOTHING)
    profession = models.ForeignKey(
        s_profession, blank=True, null=True, on_delete=models.DO_NOTHING)

    class meta:
        unique_together = ('movie', 'artist', 'profession')

    def __str__(self):
        return [self.id, self.movie, self.artist, self.profession]
    
class s_mv_cmpny(models.Model):
    ROLE_CHOICES = [("P", "Producer"), ("D", "Distributor")]
    movie = models.ForeignKey(
        s_movie, blank=True, null=True, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(
        s_company, blank=True, null=True, on_delete=models.DO_NOTHING)
    company_role = models.CharField(max_length=1,choices=ROLE_CHOICES, default='P')

    class meta:
        unique_together = ('movie_id', 'company_id','company_role')

