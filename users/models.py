from io import BytesIO
from django.contrib.auth.models import AbstractUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from PIL import Image
import sys


class MyUser(AbstractUser):
    """ User Model with Abstract User"""
    city = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255, choices=(('admin', 'Admin'),
                                                          ('customer', 'Customer')))

    def __str__(self):
        return self.username


class Profile(models.Model):
    """ Profile Model with Profile Image"""
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.webp', upload_to='images/profile/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        if self.image and self.image.size > 1000000:
            img = Image.open(self.image)
            output = BytesIO()
            img.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.image = InMemoryUploadedFile(output,
                                              'ImageField',
                                              f"{self.image.name.split('.')[0]}.jpg",
                                              'image/jpeg',
                                              sys.getsizeof(self.image),
                                              None)
        super().save(*args, **kwargs)
