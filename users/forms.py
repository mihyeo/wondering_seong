from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import User


class UserChangeForm(forms.UserChangeForm):
    password = forms.ReadOnlyPasswordHashField(
        label=_('Password')
    )

    class Meta:
        model = User
        fields = ['image', 'username', 'password']
        labels = {
            'image': "프로필 이미지",
            'username': "사용자 닉네임",
        }

    # 사용자이름 글자수 제한
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__( *args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15

    def clean_password(self):
        return self.initial["password"]