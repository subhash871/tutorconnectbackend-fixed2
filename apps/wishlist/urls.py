from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.wishlist.views import WishlistViewSet

app_name = 'wishlist'

router = DefaultRouter()
router.register(r'', WishlistViewSet, basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),
]