from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'created_at', )


# Define an inline admin descriptor for UserProfile model
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name = 'Perfil de Usuario'


# Define a new User admin
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    inlines = (UserProfileInline, )


admin.site.register(Bookmark, BookmarkAdmin)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)