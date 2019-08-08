from django.db import models
from share.timestamp import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from users.models import User
from django.shortcuts import get_object_or_404

class Board(TimeStampedModel):

    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = "공지사항"

    title = models.CharField(_('제목'), max_length=200)
    content = models.TextField(_('내용'))
    view_count = models.IntegerField(_('조회수'), default=0)

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)


class Question(TimeStampedModel):

    class Meta:
        verbose_name = "질문"
        verbose_name_plural = "질문"
        ordering = ['-created_at']

    user = models.ForeignKey(User, verbose_name=_('질문자'), on_delete=models.CASCADE)
    title = models.CharField(_('제목'), max_length=200)
    content = models.TextField(_('내용'))
    question_like_users = models.ManyToManyField(User,
                                        blank=True,
                                        related_name='question_like_users',
                                        through='QuestionLike')

    def __str__(self):
        return "Q{}. {}".format(self.pk, self.title)
    
    @property
    def answer(self):
        return get_object_or_404(Answer, question=self)

    @property
    def likes_count(self):
        return self.question_like_users.count()


class Answer(TimeStampedModel):

    class Meta:
        verbose_name = "대답"
        verbose_name_plural = "대답"

    question = models.ForeignKey(Question, verbose_name=_('질문'), on_delete=models.CASCADE)
    title = models.CharField(_('제목'), max_length=200)
    content = models.TextField(_('내용'))

    def __str__(self):
        return "A. {}".format(self.title)


class QuestionLike(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name=_('작성자'), on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name=_('질문'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '질문 좋아요'
        verbose_name_plural = '질문 좋아요'
        unique_together = (
            ('user', 'question')
        )