from django.urls import path
from . import views



urlpatterns = [

    path('subcontinents/', views.SubcontinentListView.as_view(), name='subcontinents'),
    path('subcontinent/<int:pk>', views.SubcontinentDetailView.as_view(), name='subcontinent-detail'),

    path('asias/', views.AsiaListView.as_view(), name='asias'),
    path('asia/<int:pk>', views.AsiaDetailView.as_view(), name='asia-detail'),

    path('middleeasts/', views.MiddleEastListView.as_view(), name='middleeasts'),
    path('middleeast/<int:pk>', views.MiddleEastDetailView.as_view(), name='middleeast-detail'),

    path('unitedstates/', views.UnitedStateListView.as_view(), name='unitedstates'),
    path('unitedstate/<int:pk>', views.UnitedStateDetailView.as_view(), name='unitedstate-detail'),

    path('europes/', views.EuropeListView.as_view(), name='europes'),
    path('europe/<int:pk>', views.EuropeDetailView.as_view(), name='europe-detail'),

    path('internationalorganizations/', views.InternationalOrganizationListView.as_view(), name='internationalorganizations'),
    path('internationalorganization/<int:pk>', views.InternationalOrganizationDetailView.as_view(), name='internationalorganization-detail'),

]
