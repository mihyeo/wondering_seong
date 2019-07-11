from django.db import models
from share.timestamp import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

class Board(TimeStampedModel):

    class Meta:
        verbose_name = '공지'
        verbose_name_plural = "공지사항"

    title = models.CharField(_('제목'), max_length=200)
    content = models.TextField(_('내용'))
    view_count = models.IntegerField(_('조회수'), default=0)