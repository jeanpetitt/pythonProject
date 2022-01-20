from django.contrib import admin
from .models import Repetiteur
from .models import Client
from .models import Classe
from .models import Matiere
from .models import Cours

# Register your models here.
admin.site.register(Repetiteur)
admin.site.register(Client)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Cours)
