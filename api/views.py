from django.shortcuts import render

from . import exc, resp, serializers, use_cases
from rest_framework import response, views
from django.http import *


class RecruitmentAPIView(views.APIView):
    def get(self, request):  
        recruitments = serializers.RecruimentSerializer(
            use_cases.get_recruitments(),
            many=True,
        )

        return response.Response(recruitments.data)


class EnrolleeAPIView(views.APIView):
    def get(self, request, snils):
        try:
            enrollee = serializers.EnrolleeSerializer(
                use_cases.get_enrollee(snils)
            )
            return response.Response(enrollee.data)
        except(exc.EnrolleeNotFound):
            raise resp.EnrolleNotFound()
        except(exc.EnrolleeDoesNotHavePrioritySpeciality):
            raise resp.EnrolleeDoesNotHavePrioritySpeciality()


class SpecialityAPIView(views.APIView):
    def get(self, request):  
        specialities = serializers.SpecialitySerializer(
            use_cases.get_specialities(),
            many=True,
        )

        return response.Response(specialities.data)
