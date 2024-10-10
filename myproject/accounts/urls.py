from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/create/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]
