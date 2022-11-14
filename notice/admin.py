from django.contrib import admin
from .models import galleries, noticeboard, teacher, testimonial

# Register your models here.
admin.site.register(noticeboard)
admin.site.register(galleries)
admin.site.register(teacher)
admin.site.register(testimonial)
