from django.urls import path
from polls.views import homePage, questionDetails, register, loginPage, logoutPage

urlpatterns = [
    path('', homePage, name='home'),
    path('<int:questionId>/', questionDetails, name='question_details'),
    path('register/', register, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutPage, name="logout"),
]
