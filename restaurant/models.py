from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator


STATUS = ((0, "Draft"), (1, "Published"))

class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking")
    first_name = models.TextField()
    last_name = models.TextField()
    num_guests = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(23)]
    )
    date = models.DateField()
    time = models.TimeField()
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'''Booking: {self.id} - User: {self.user}, 
               Name: {self.first_name} {self.last_name}, 
               Date: {self.date}, Time: {self.time}, 
               Guests: {self.num_guests}, 
               Note: {self.content}'''

