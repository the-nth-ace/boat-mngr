from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Owner(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO
    # BUSINESS

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("owner_detail", kwargs={"pk": self.pk})


