from django.urls import path
from . import views
urlpatterns = [
    # Todos
    path('todo/', views.TodoListCreate.as_view()),
    path('todo/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todo/<int:pk>/complete', views.TodoComplete.as_view()),
    path('todo/completed/', views.TodoCompletedList.as_view()),

    # Auth
    path('signup', views.signup),
    path('login', views.login),
]