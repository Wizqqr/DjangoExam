from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.ClothListView.as_view(), name='shop'),
    path('shop/young/', views.YoungClothListView.as_view(), name='young'),
    path('shop/old/', views.OldClothListView.as_view(), name='old'),
    path('shop/<int:id>/', views.ClothDetailView.as_view(), name='detail_view'),
]