from django.urls import path
from . import views

urlpatterns = [
    path('shop_list/', views.GadgetListView.as_view(), name='shop_list'),
    path('shop_list/<int:id>/', views.GadgetDetailForm.as_view(), name='shop_detail'),
    path('shop_list/comment/', views.GadgetCreateComment.as_view(), name='create_comment'),
    # path('phone_list/', views.PhoneListView.as_view(), name='phone_list'),
    # path('phone_list/<int:id>/', views.PhoneDetailForm.as_view(), name='phone_detail'),
    # path('phone_list/<int:id>/delete/', views.PhoneDeleteForm.as_view(), name='phone_detail_delete'),
    # path('phone_list/<int:id>/update/', views.PhoneEditForm.as_view(), name='phone_update_view'),
    # path('create_phone/', views.PhoneCreateForm.as_view(), name='create_phone'),
    # path('phone_list/comment/', views.PhoneCreateComment.as_view(), name='create_comment'),
    # path('search/', views.SearchPhoneView.as_view(), name='phone_search'),
]