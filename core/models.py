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
    name = models.CharField(max_length=255, unique=True)
    owner = models.CharField(max_length=255)
    operation_commenced = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.name

    @property
    def boats(self):
        return Boat.objects.filter(business=self).count()

    @property
    def reviews(self):
        boats = Boat.objects.filter(business=self)
        reviews = [Review.objects.filter(boat=boat).count() for boat in boats]
        return sum(reviews)

    # class Meta:
    #     ordering =['-']

    @property
    def average_rating(self):
        return 4.5


class Boat(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    captain_name = models.CharField(max_length=100)
    captain_photo = models.ImageField(upload_to="images/")
    deckhand = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
    @property
    def deckhand_photo(self):
        number = self.name[-1]
        return f'D{number}'


class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    content = models.TextField()
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
