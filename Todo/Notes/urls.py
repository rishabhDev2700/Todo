from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.create_user, name='create_user'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.add_note, name='add'),
    path('delete/<int:note_id>', views.delete, name='delete')
]
