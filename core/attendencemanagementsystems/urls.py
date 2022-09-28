from django.urls import path


from .views import *


app_name = 'attendencemanagementsystems'

urlpatterns = [
    path('register/', UserRegister.as_view()),
    path('login/', Login.as_view(), name='login'),
    path('create/', PostCreateView.as_view()),
    path('list/', PostDetailView.as_view()),
    path('detail/<int:pk>/', PostDetailView.as_view()),
    path('creategenerics/', Create.as_view()),
    path('listgenerics/', List.as_view()),
    path('retrieve/<int:pk>', Retrieve.as_view()),

]
