from django.db import models
from django.template.defaultfilters import slugify

class User_profile(models.Model):
    prof_pic = models.ImageField(upload_to="images", null=True, blank=True)
    prof_description = models.CharField(max_length=20)

    def __str__(self):
        return self.prof_description

class Projects(models.Model):
    proj_id = models.AutoField(primary_key=True)
    proj_img = models.ImageField(upload_to="images", null=True, blank=True)
    proj_name = models.CharField(max_length=15)
    proj_description = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f'{self.proj_id}{" "}{self.proj_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.proj_name}+{self.proj_id}')
        super().save(*args, **kwargs)


class Skills(models.Model):
    skill_title = models.CharField(max_length=20)
    skill_description = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_title