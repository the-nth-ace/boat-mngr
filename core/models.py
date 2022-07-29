from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from PIL import Image


class Operator(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_info = models.CharField(max_length=255)
    operation_commenced = models.IntegerField()

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.name

    @property
    def boats(self):
        return Boat.objects.filter(operator=self).count()

    @property
    def reviews(self):
        boats = Boat.objects.filter(operator=self)
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
    captain_certificaiton = models.CharField(max_length=1000, default="")
    captain_photo = models.ImageField(upload_to="captains/")
    deckhand_name = models.CharField(max_length=100)
    deckhand_photo = models.ImageField(upload_to="deckhand/")
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    niwa_approval_date = models.DateField()
    laswa_approval_date = models.DateField()
    certification_status = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

    @property
    def reviews(self):
        return Review.objects.filter(boat=self).order_by("created")


class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    content = models.TextField()
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
