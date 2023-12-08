from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    num_guests = models.PositiveIntegerField()
    date = models.DateTimeField()
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Booking {self.id} - Date: {self.date}, User: {self.user}"


class Review(models.Model):
    booking = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews")
    stars = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stars", blank=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Review {self.content}, by {self.user}"
