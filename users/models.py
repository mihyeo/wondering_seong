from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    image = ImageField(_("Image of User"), upload_to="image/")
    followings = ManyToManyField("self", related_name='followers', symmetrical=False)
    