from django.contrib import admin

from .models import Profile
from .models import Work,Exprience,Education,Software,Technical

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Education)
admin.site.register(Exprience)
admin.site.register(Software)
admin.site.register(Technical)



