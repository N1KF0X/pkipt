from rest_framework import serializers

from . import models, use_cases


class SelectedSpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnrolleeSpeciality
        fields = ['speciality', 'is_priority', 'is_enrolled']


class EnrolleeSerializer(serializers.ModelSerializer):
    selected_specialities = SelectedSpecialitySerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField('get_rating')

    def get_rating(self, enrollee):
        return use_cases.calculate_rating(enrollee.snils)

    class Meta:
        model = models.Enrollee
        fields = ['full_name', 'snils', 'inn', 'gpa', 'application_date', 'selected_specialities', 'rating']


class RecruimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recruitment
        fields = ['name', 'closing_date']


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Speciality
        fields = ['code', 'name', 'seats_amount', 'education_period']