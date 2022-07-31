import os
from django.db import models
from django.urls import reverse


class Operator(models.Model):
    class AssociationChoices(models.TextChoices):
        ATBOWATON = (
            "atbo",
            "Association of Tourists Boat Operators and Water Transporters of Nigeria",
        )
        UFTA = "ufta", "United Ferry Transporters' Association"
        IBOA = "iboa", "Integrated Boat Operators Association"

    name = models.CharField(max_length=255, unique=True)
    contact_info = models.CharField(max_length=255)
    operation_commenced = models.IntegerField()
    association = models.CharField(
        max_length=4,
        choices=AssociationChoices.choices,
        default=AssociationChoices.ATBOWATON,
    )

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("dashboard_operator_detail", kwargs={"pk": self.pk})

    @property
    def boats(self):
        return Boat.objects.filter(operator=self).count()

    @property
    def reviews(self):
        boats = Boat.objects.filter(operator=self)
        reviews = [Review.objects.filter(boat=boat).count() for boat in boats]
        return sum(reviews)

    @property
    def average_rating(self):
        return 4.5


class Boat(models.Model):
    class Meta:
        unique_together = ["name", "operator"]

    def rename_captain_boat_photo_path(instance, filename) -> str:
        basefilename, file_extension = os.path.splitext(filename)
        return f"mediafiles/captains/{instance.operator.name.lower()}_{instance.name.lower()}{file_extension}"

    def rename_deckhand_boat_photo_path(instance, filename) -> str:
        basefilename, file_extension = os.path.splitext(filename)
        return f"mediafiles/deckhands/{instance.operator.name.lower()}_{instance.name.lower()}{file_extension}"

    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    captain_name = models.CharField(max_length=100)
    captain_certification = models.CharField(max_length=1000, default="")
    captain_photo = models.ImageField(upload_to=rename_captain_boat_photo_path)
    deckhand_name = models.CharField(max_length=100)
    deckhand_photo = models.ImageField(upload_to=rename_deckhand_boat_photo_path)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    niwa_approval_date = models.DateField()
    laswa_approval_date = models.DateField()
    certification_status = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

    @property
    def reviews(self):
        return Review.objects.filter(boat=self).order_by("created")

    @property
    def reviews_count(self):
        return self.reviews.count()


class Review(models.Model):
    class Meta:
        ordering = ["-created"]

    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    content = models.TextField()
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reviewer_name
