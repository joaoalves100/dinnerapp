from django.contrib import admin
from .models import Meals
from .models import People
from .models import Participation

# Register your models here.
admin.site.register(Meals)
admin.site.register(People)
admin.site.register(Participation)
