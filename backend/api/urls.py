from django.urls import path
from .views import PredictDigitView

urlpatterns = [
    path('predict/', PredictDigitView.as_view(), name='predict_digit'),
]