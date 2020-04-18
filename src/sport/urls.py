from django.urls import path
from . import views





urlpatterns = [

    path('crickets/', views.CricketListView.as_view(), name='crickets'),
    path('cricket/<int:pk>', views.CricketDetailView.as_view(), name='cricket-detail'),

    path('footballs/', views.FootballListView.as_view(), name='footballs'),
    path('football/<int:pk>', views.FootballDetailView.as_view(), name='football-detail'),

    path('tennises/', views.TennisListView.as_view(), name='tennises'),
    path('tennis/<int:pk>', views.TennisDetailView.as_view(), name='tennis-detail'),

    path('swimmings/', views.SwimmingListView.as_view(), name='swimmings'),
    path('swimming/<int:pk>', views.SwimmingDetailView.as_view(), name='swimming-detail'),

    path('hockies/', views.HockeyListView.as_view(), name='hockies'),
    path('hockey/<int:pk>', views.HockeyDetailView.as_view(), name='hockey-detail'),

]
