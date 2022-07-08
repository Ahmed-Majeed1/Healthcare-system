from django.db import models
from django.contrib.auth.models import User
from PIL import Image
  

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.TextField()
    email = models.EmailField(max_length=50)
    weight = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    previous_illness = models.TextField()
    chronic_diseases = models.TextField()
    addictions = models.TextField()
    blood_type = models.CharField(max_length=5)
    allergy = models.TextField()
    current_meds = models.TextField()
    previous_surgeries = models.TextField()
    disabilities = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
