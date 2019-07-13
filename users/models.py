from django.contrib.auth.models import AbstractUser
from share.timestamp import TimeStampedModel
from django.db.models import *
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser, TimeStampedModel):
    image = ImageField(_("프로필사진"), upload_to="image/", null=True, blank=True)
    followings = ManyToManyField("self", related_name='followers', symmetrical=False)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = "사용자"
    