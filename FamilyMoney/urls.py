from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, api

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('home_json/', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('add_family_member/<int:user_id>/',
         views.add_family_member, name='add_family_member'),
    path('remove_family_member/<int:family_member_id>/',
         views.remove_family_member, name='remove_family_member'),
    path('list/', views.list_users, name='list'),
    path('api/add_family_member/<int:user_id>/',
         api.AddFamilyMemberAPI.as_view(), name='add_family_member_api'),


]
