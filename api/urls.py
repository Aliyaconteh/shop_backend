from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, PurchaseListCreateView, PurchaseDetailView

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),


    path('purchase/', PurchaseListCreateView.as_view(), name='purchase-list-create'),
    path('purchase/<int:pk>/', PurchaseDetailView.as_view(), name='purchase-detail'),
]
