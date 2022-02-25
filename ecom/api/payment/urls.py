from django.urls import path, include

from . import views

urlpatterns = [
    path('get-token/<str:id>/<str:token>/', views.generate_token, name='token.generate'),
    path('process-payment/<str:id>/<str:token>/', views.process_payment, name='payment.process'),
]