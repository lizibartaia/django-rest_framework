from . import views
from django.urls import path

urlpatterns = [
    path('',views.NoteCollectionView.as_view()),
    path('<int:pk>/',views.NoteSingletonView.as_view()),
     
]