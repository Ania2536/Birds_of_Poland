from django.contrib import admin

# Register your models here.
from birds_app.models import Family, Region, Birds, Images, Comments, Wishlist, Quiz, Question, Answer, Carousel

admin.site.register(Family)
admin.site.register(Region)
admin.site.register(Birds)
admin.site.register(Images)
admin.site.register(Comments)
admin.site.register(Wishlist)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Carousel)
