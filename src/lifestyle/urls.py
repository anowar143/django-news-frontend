from django.urls import path
from . import views



urlpatterns = [

    path('healths/', views.HealthListView.as_view(), name='healths'),
    path('health/<int:pk>', views.HealthDetailView.as_view(), name='healths-detail'),

    path('fashions/', views.FashionListView.as_view(), name='fashions'),
    path('fashion/<int:pk>', views.FashionDetailView.as_view(), name='fashion-detail'),

    path('cooks/', views.CookListView.as_view(), name='cooks'),
    path('cook/<int:pk>', views.CookDetailView.as_view(), name='cook-detail'),

]
