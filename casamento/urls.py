from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ConvidadoViewSet, PresenteViewSet, CompraViewSet

router = DefaultRouter()
router.register(r'convidados', ConvidadoViewSet)
router.register(r'presentes', PresenteViewSet)
router.register(r'compras', CompraViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('presentes/<int:pk>/lojas/', PresenteViewSet.as_view({'get': 'get_lojas'}), name='presente-lojas'),
]
