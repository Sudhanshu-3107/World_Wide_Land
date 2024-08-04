from django.contrib import admin
from .models import Agent, PropertyOwner, Property, PropertyQuery, PropertySeeker, Feedback, Inquiry, Member
# Register your models here.

admin.site.register(Agent)
admin.site.register(PropertySeeker)
admin.site.register(Property)
admin.site.register(PropertyQuery)
admin.site.register(PropertyOwner)
admin.site.register(Inquiry)
admin.site.register(Feedback)
admin.site.register(Member)