from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

class Region(models.Model):
    region = models.CharField(max_length=24)

    def __str__(self):
        return self.region

class Birds(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField(default="")
    population = models.IntegerField(null=True)
    region = models.ManyToManyField(Region)
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_main_image_url(self):
        image = self.images_set.get(main=True)
        if image.image is None:
            return ""
        return image.image.url


class Images(models.Model):
    bird = models.ForeignKey(Birds, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True) # null = baza danych / blank = formularz
    description = models.TextField(default="")
    main = models.BooleanField(default=False)

    def __str__(self):
        return str(self.bird)

class Comments(models.Model):
    birds = models.ForeignKey(Birds, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment on {self.birds} by {self.author}'

class Wishlist(models.Model):
    birds = models.ForeignKey(Birds, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.birds} by {self.user}'

class Quiz(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name or ''

class Question(models.Model):
    question = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

class Carousel(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=150)
    action_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title