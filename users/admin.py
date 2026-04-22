from django.contrib import admin

from users.models import User

admin.site.register(User)
#admin.site.register(Products)

# @admin.register(Categories)
# class CategoriesAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}
