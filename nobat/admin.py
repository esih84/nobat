from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
# Now register the new UserAdmin...
admin.site.register(MyUser)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
