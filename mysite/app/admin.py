from django.contrib import admin

from .models import Profile
from .models import Work,Exprience,Education

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Exprience)


