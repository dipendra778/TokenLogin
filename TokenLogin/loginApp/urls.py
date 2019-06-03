
from django.urls import path,include
from rest_framework.authtoken import views
from .views import LoginViewSet,NestedViewSet
from rest_framework import routers
router=routers.DefaultRouter()
router.register('login',LoginViewSet)
router.register('nested',NestedViewSet)
urlpatterns = [
    path('api/',views.obtain_auth_token,name="login"),
    path('data/',include(router.urls))
]