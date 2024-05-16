from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/enrollees/<str:snils>', views.EnrolleeAPIView.as_view()),
    path('api/recruitmets', views.RecruitmentAPIView.as_view()),
    path('api/specialities', views.SpecialityAPIView.as_view()),
]