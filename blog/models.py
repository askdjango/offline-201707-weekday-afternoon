import os
import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


def min_length_3(value):
    if len(value) < 3:
        raise ValidationError('3글자 이상 입력해주세요.')


def random_upload_to(instance, orig_filename):
    # 파일명을 포함한 모든 경로를 기대
    ext = os.path.splitext(orig_filename)[-1].lower()
    filename = uuid.uuid4().hex + ext
    filepath = os.path.join(filename[:3], filename[3:6], filename[6:9], filename[9:])
    return filepath


class Post(models.Model):
    author = models.CharField(max_length=20, help_text='포스팅 작성자 이름을 입력해주세요.')
    title = models.CharField(max_length=100, validators=[min_length_3])
    content = models.TextField()
    photo = models.ImageField(upload_to=random_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        # '/weblog/{}/'.format(self.id)
        return reverse('blog:post_detail', args=[self.id])
        # return reverse('blog:post_detail', kwargs={'pk': self.id})

