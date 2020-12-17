from django.db import models

PREFIX_CHOICES = {
    ("Miss", "Miss"),
    ("Mr.", "Mr."),
    ("Mrs.", "Mrs."),
    ("Ms.", "Ms"),

}


# Create your models here.
class UserProfile(models.Model):
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES)
    firstName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    objects = models.Manager()

    def __str__(self):
        return self.firstName
