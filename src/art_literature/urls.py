from django.urls import path
from . import views



urlpatterns = [

    path('poetries/', views.PoetryListView.as_view(), name='poetries'),
    path('poetry/<int:pk>', views.PoetryDetailView.as_view(), name='poetry-detail'),

    path('stories/', views.StoryListView.as_view(), name='stories'),
    path('story/<int:pk>', views.StoryDetailView.as_view(), name='story-detail'),

    path('novels/', views.NovelListView.as_view(), name='novels'),
    path('novel/<int:pk>', views.NovelDetailView.as_view(), name='novel-detail'),

]
