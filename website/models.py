from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250, null=True, blank=True)
    profile_pic = models.FileField(upload_to="profile/", null=True, blank=True)

    def __str__(self):
        return self.name


class Contest(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    image = models.FileField(upload_to="contest_thumbnail/", null=True, blank=True)
    description = models.TextField()
    status = models.CharField(choices=[('active', 'active'), ('ended', 'ended')], max_length=250)
    winner = models.CharField(max_length=250, null=True, blank=True)
    winner_image = models.FileField(upload_to="winner_image/", null=True, blank=True)
    slug = models.CharField(max_length=250, help_text="this-is-slug")
    availble_seat = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class JoinContest(models.Model):
    id = models.AutoField(primary_key=True)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.contest)

class SubmitLogo(models.Model):
    id = models.AutoField(primary_key=True)    
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="file/", null=True, blank=True)


class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Results_banner(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField(upload_to="results/", blank=True, null=True)

    def __str__(self):
        return str(self.image)


class About(models.Model):
    banner = models.FileField(upload_to="about/", null=True, blank=True)
    heading = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.heading

class Contact(models.Model):    
    name = models.CharField(max_length=250)    
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name
    