from django.urls import path
from .views import RegisterView, LoginView, AddSolvedProblemView, CheckSolvedProblemView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/<str:username>/add_solved_problem/', AddSolvedProblemView.as_view(), name='add_solved_problem'),
    path('users/<str:username>/check_solved_problem/<int:problem_id>/', CheckSolvedProblemView.as_view(), name='check_solved_problem'),
]
