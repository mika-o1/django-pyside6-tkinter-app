from django.urls import path
from app_teacher.views import login, home, register, api_result, api_result_id

urlpatterns = [
    path(route='', view=home, name=""),
    path(route='home/', view=home, name="home"),

    path(route='login/', view=login, name="login"),
    path(route='register/', view=register, name="register"),

    # читаем все рецепты
    path(route='api/result/', view=api_result, name="api_result"),

    # читаем рецепты по id
    path(route='api/result/<int:recept_id>/', view=api_result_id, name="api_result_id"),
]
