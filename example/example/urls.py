"""example URL Configuration"""

from django.urls import include, re_path
from django.contrib import admin
from rest_framework import routers
from example import views

router = routers.DefaultRouter()
router.register(r'talks', views.TalkViewSet)

urlpatterns = [
    re_path('', include(router.urls)),
    re_path(r'^admin/', admin.site.urls),
]
