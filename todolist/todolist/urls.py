from django.contrib import admin
from django.urls import include, path
from todolist.views import todoappView, addTodoView, deleteTodoView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', todoappView),
    path('addTodoItem/',addTodoView), 
    path('deleteTodoItem/<int:i>/', deleteTodoView),
]