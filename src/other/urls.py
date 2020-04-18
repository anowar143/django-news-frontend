from django.urls import path
from . import views





urlpatterns = [

    path('ramadans/', views.RamadanListView.as_view(), name='ramadans'),
    path('ramadan/<int:pk>', views.RamadanDetailView.as_view(), name='ramadan-detail'),

    path('features/', views.FeatureListView.as_view(), name='features'),
    path('feature/<int:pk>', views.FeatureDetailView.as_view(), name='feature-detail'),

]
