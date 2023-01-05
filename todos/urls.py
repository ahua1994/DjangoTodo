from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api", TodoMVS)

urlpatterns = [
    path("", home),
    path("list/", todos_get),
    path("add/", todos_add),
    path("todos/create/", TodoListCreate.as_view()),
    path("todos/<int:pk>/", TodoGetUpdateDelete.as_view())
] + router.urls
