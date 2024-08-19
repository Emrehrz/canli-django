from django.apps import AppConfig
#▰------------------------------------------------------------------------------------------------
import os
from django.utils.translation import gettext_lazy as _
#------------------------------------------------------------------------------------------------▰

class UygulamaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uygulama'
    #▰------------------------------------------------------------------------------------------------
    verbose_name = _('Uygulama')

    def ready(self):
        # Uygulama başladığında çalışacak
        self.setup_locale_paths()

    def setup_locale_paths(self):
        # Uygulama dizini içinde locale adlı dizini oluşturmak
        locale_path = os.path.join(os.path.dirname(__file__), 'locale')
        if not os.path.exists(locale_path):
            os.makedirs(locale_path)
    #------------------------------------------------------------------------------------------------▰