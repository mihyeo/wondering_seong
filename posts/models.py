from django.db import models
from users.models import User
from share.timestamp import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class Post(TimeStampedModel):

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = "게시글"
        ordering = ['-created_at']

    POST_KIND_CHOICES = [
        (0, "card"),
        (1, "post")
    ]
    POST_CATEGORY_CHOICES = [
        (0, "basic"),
        (1, "before_sex"),
        (2, "sex_ing"),
        (3, "after_sex"),
        (4, "news")
    ]
    
    user = models.ForeignKey(User, verbose_name=_('글쓴이'), on_delete=models.CASCADE)
    title = models.CharField(_('제목'), max_length=200)
    content = models.TextField(_('내용'))
    kinds = models.PositiveSmallIntegerField(_('타입'), choices=POST_KIND_CHOICES)
    category = models.PositiveSmallIntegerField(_('카테고리'), choices=POST_CATEGORY_CHOICES)
    view_count = models.IntegerField(_('조회수'), default=0)
    image = models.ImageField(_('대표이미지'), null=True, upload_to="image/", blank=True)
    like_users = models.ManyToManyField(User,
                                        blank=True,
                                        related_name='like_users',
                                        through='Like')
    
    def __str__(self):
        return self.title

    @property	
    def card_images(self):	
        return CardImage.objects.filter(post=self).order_by('position')

    @property
    def comments(self):
        return Comment.objects.filter(post=self)

    @property
    def likes_count(self):
        return self.like_users.count()
    

class CardImage(TimeStampedModel):

    class Meta:
        verbose_name = '게시글 이미지'
        verbose_name_plural = "게시글 이미지"

    post = models.ForeignKey(Post, verbose_name=_('게시글'), on_delete=models.CASCADE)
    image = models.ImageField(_('이미지'), upload_to="image/")
    position = models.PositiveIntegerField(_('순서'), null=True, blank=True)
    
    def __str__(self):
        return "{} : {}의 이미지".format(self.pk, self.post.title)
    

class Comment(TimeStampedModel):

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = "댓글"
        ordering = ['-created_at']

    user = models.ForeignKey(User, verbose_name=_('작성자'), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_('게시글'), on_delete=models.CASCADE)
    body = models.TextField(_('내용'))


class Like(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name=_('작성자'), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_('게시글'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = '게시글 좋아요'
        verbose_name_plural = '게시글 좋아요'
        unique_together = (
            ('user', 'post')
        )