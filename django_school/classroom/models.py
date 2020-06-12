from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    city = models.CharField(max_length=32, null=True)
    image_profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    description = models.TextField(null = True, blank = True)

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null = True)
    price = models.IntegerField()
    slug = models.SlugField(null = False, blank = False, unique = True)
    image = models.ImageField(upload_to='subjects/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

def set_slug(sender, instance, *args, **kargs):
    if instance.name and not instance.slug:
        slug = slugify(instance.name)

        while Subject.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.name, str(uuid.uuid4())[:8])
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Subject)
   
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    interests = models.ManyToManyField(Subject, related_name='subject_teacher')

    def __str__(self):
        return "{}: {}".format(self.user, self.interests)
