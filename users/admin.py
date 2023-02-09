from django.contrib import admin

from users.models import MyUser, Profile


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'city', 'user_type')
    list_filter = ('city', 'user_type')
    search_fields = ('first_name', 'last_name', 'username', 'city')


admin.site.register(MyUser, UserAdmin)
admin.site.register(Profile)
