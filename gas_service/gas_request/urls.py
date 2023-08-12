from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('create_request/', views.Create_request, name='create_request'),
    path('track_request/', views.track_request, name='track_request'),
    path('mark_completed/', views.mark_completed, name='mark_completed'),
    path('update_request/<int:id>', views.update_request, name='update_request')

]