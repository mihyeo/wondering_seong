from django.db import models
from share.timestamp import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from users.models import User

class Board(TimeStampedModel):

    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = "공지사항"

    title = models.CharField(_('제목'), max_length=200)
    content = models.TextField(_('내용'))
    view_count = models.IntegerField(_('조회수'), default=0)


class Question(TimeStampedModel):

    class Meta:
        verbose_name = "질의응답"
        verbose_name_plural = "질의응답"

    user = models.ForeignKey(User, verbose_name=_('질문자'), on_delete=models.CASCADE)
    title = models.CharField(_('제목'), max_length=200)
    content = models.TextField(_('내용'))