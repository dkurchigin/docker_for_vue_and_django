from django.urls import path, include
from rest_framework import routers
from mainapp import views

app_name = 'mainapp'

router = routers.DefaultRouter()
router.register(r'pois', views.POIView, 'pois')

urlpatterns = [
    path('api/', include(router.urls)),
]
