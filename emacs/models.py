from django.conf import settings
from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=128,
                            unique=True)
    description = models.TextField()
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 blank=True,
                                 related_name='user_add')
    screenshot = models.ImageField(upload_to='screenshots',
                                   null=True,
                                   blank=True)
    download_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-download_count']
        abstract = True

    def human_readable_download_count(self):
        '''Should return human readable count
        '''
        pass

    def __str__(self):
        return self.__class__.__name__


class Code(CommonInfo):
    gist_url = models.URLField(max_length=100,
                               null=True,
                               blank=True)
    code = models.TextField()
