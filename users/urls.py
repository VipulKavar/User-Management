from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users import views

app_name = 'user_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('user/list/a/', views.UserListView.as_view(), name='list'),
    path('user/create/a/', views.UserCreateView.as_view(), name='create'),
    path('user/update/<int:pk>/a/', views.UserUpdateView.as_view(), name='update'),
    path('user/delete/<int:pk>/a/', views.UserDeleteView.as_view(), name='delete'),
    path('user/register/c/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('user/profile/<int:pk>/c/', views.UserProfile.as_view(), name='profile'),
]
