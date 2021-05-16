from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'materials',views.MaterialsViewSet)
router.register(r'troops',views.TroopsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework'))
]