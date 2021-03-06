from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField


neighborhood = (
        ('1', 'Vaal'),
        ('2', 'Red Cross'),
        ('3', 'The Park'),
        ('4', 'BEACH'),
        ('5', 'BMW'),
        ('6', 'Deer'),
        ('7', 'Kenya Police'),
        ('8', 'She Wolf'),
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    neighborhood = models.CharField(max_length=25,choices=neighborhood, default='Red Ville')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
