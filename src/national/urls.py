from django.urls import path
from . import views





urlpatterns = [

    path('politics/', views.PoliticListView.as_view(), name='politics'),
    path('politic/<int:pk>', views.PoliticDetailView.as_view(), name='politic-detail'),

    path('crimes/', views.CrimeListView.as_view(), name='crimes'),
    path('crime/<int:pk>', views.CrimeDetailView.as_view(), name='crime-detail'),

    path('administrations/', views.AdministrationListView.as_view(), name='administrations'),
    path('administration/<int:pk>', views.AdministrationDetailView.as_view(), name='administration-detail'),

    path('parliaments/', views.ParliamentListView.as_view(), name='parliaments'),
    path('parliament/<int:pk>', views.ParliamentDetailView.as_view(), name='parliament-detail'),

    path('economics/', views.EconomicListView.as_view(), name='economics'),
    path('economic/<int:pk>', views.EconomicDetailView.as_view(), name='economic-detail'),

    path('educations/', views.EducationListView.as_view(), name='educations'),
    path('education/<int:pk>', views.EducationDetailView.as_view(), name='education-detail'),

    path('weathers/', views.WeatherListView.as_view(), name='weathers'),
    path('weather/<int:pk>', views.WeatherDetailView.as_view(), name='weather-detail'),

]

