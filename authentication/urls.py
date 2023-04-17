from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, LocationViewSet

router  = SimpleRouter()
router.register(r'', UserViewSet)
router.register(r'location', LocationViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
] + router.urls