from django.contrib import admin

# Register your models here.
from .models import Practice
admin.site.register(Practice)

from .models import Blogpost
admin.site.register(Blogpost)