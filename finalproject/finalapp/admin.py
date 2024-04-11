from django.contrib import admin
from . models import Marvel,Dccomics,Monster,Review,MReview,DReview
# Register your models here.
admin.site.register(Marvel)
admin.site.register(Dccomics)
admin.site.register(Monster)
# admin.site.register(user_details)
admin.site.register(Review)
admin.site.register(MReview)
admin.site.register(DReview)