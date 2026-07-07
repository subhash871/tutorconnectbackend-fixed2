from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['student', 'teacher', 'created_at']
    search_fields = ['student__email', 'teacher__user__email']
