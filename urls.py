# writing_assignment/tasks/urls.py

from django.urls import path
from .views import assignment_list, create_assignment, assignment_detail, update_assignment, delete_assignment

urlpatterns = [
    path('assignment/', assignment_list, name='assignment_list'),
    path('assignment/<int:assignment_id>/', assignment_detail, name='assignment_detail'),
    path('assignment/create/', create_assignment, name='create_assignment'),
    path('assignment/<int:assignment_id>/update/', update_assignment, name='update_assignment'),
    path('assignment/<int:assignment_id>/delete/', delete_assignment, name='delete_assignment'),
]
