from django.db import models
from django.contrib.auth.models import User

class Job_category(models.Model):
    id = models.AutoField(primary_key=True)
    name_job = models.CharField(max_length=50)

    def __str__(self):
        return self.name_job

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='photos')
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    jobtitle = models.ForeignKey(Job_category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Profile of {self.user.username}"


