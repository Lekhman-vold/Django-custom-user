from django.urls import path
from .views import UserForm


urlpatterns = [
    path('form/', UserForm.as_view()),
]
