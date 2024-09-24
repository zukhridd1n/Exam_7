from django.db import models


class Games(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    start_date = models.DateField()
    rating =models.IntegerField()

class Countries(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    start_date = models.DateField()
    flag = models.ImageField(upload_to="flags/%Y/%m/%d")


class Football_club(models.Model):
    name = models.CharField(max_length=100)
    flag  = models.ImageField(default='')
    point = models.ImageField(default=0)
    slug = models.SlugField(max_length=100, unique=True)
    start_date = models.DateField()
    rating =models.IntegerField()
    players_count = models.IntegerField()
    salary = models.IntegerField()
    games = models.ManyToManyField(Games)
    countries = models.ManyToManyField(Countries)


class Championships_football(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to="championships/%Y/%m/%d")
    start_date = models.DateField()
    rating =models.IntegerField()
    clubs_count = models.IntegerField()
    countries = models.ManyToManyField(Countries)
    clubs = models.ManyToManyField(Football_club)

class Players_football(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to="players/%Y/%m/%d")
    start_date = models.DateField()
    age = models.IntegerField()
    rating = models.IntegerField()
    salary = models.IntegerField()
    football_clubs = models.ManyToManyField(Football_club)


class Fovorite_games(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)


class Championships_tennis(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to="championships/%Y/%m/%d")
    start_date = models.DateField()
    rating =models.IntegerField()

class Tennis_players(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    avatar = models.ImageField(upload_to="players/%Y/%m/%d")
    start_date = models.DateField()
    rating = models.IntegerField()


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    country = models.ManyToManyField(Countries)
    games = models.ManyToManyField(Games)



class League (models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)












