from django.urls import path
from .views import upload_and_predict

urlpatterns = [
    path('', upload_and_predict, name='upload_and_predict'),
]
