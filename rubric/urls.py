from django.urls import path

from .views import by_rubric

app_name = 'rubric'

urlpatterns = [
    path('<int:pk>', by_rubric, name='by_rubric'),
]
