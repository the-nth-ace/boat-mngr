from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# class Owner(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # TODO
#     # BUSINESS

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("owner_detail", kwargs={"pk": self.pk})


class Business(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    operation_commenced = models.DateField()
    # total_boats = models.ForeignKey(Boat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering =['-']


class Boat(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    captain_name = models.CharField(max_length=100)
    captain_photo = models.ImageField()
    deckhand = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    content = models.TextField()
    Boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name