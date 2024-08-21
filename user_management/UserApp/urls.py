from django.urls import path
from .views import view_users, add_user, update_user, delete_user

urlpatterns = [  
    path('', view_users, name='view_users'),  
    path('add/', add_user, name='add_user'),  
    path('update/<int:user_id>/', update_user, name='update_user'),  
    path('delete/<int:user_id>/', delete_user, name='delete_user'),  
] 