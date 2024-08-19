from django.db import models
from django.utils.translation import gettext_lazy as _


class Uygulama(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Uygulama')
        verbose_name_plural = _('Uygulamalar')
    pass
