from django.contrib import admin

from . import models, use_cases


class EnrolleeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'snils', 'inn', 'gpa', 'recruitment', 'application_date']
    search_fields = ['full_name', 'snils', 'inn', 'gpa', 'application_date']
    list_filter = ['recruitment']


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'education_period', 'seats_amount']
    search_fields = ['code', 'name']
    list_filter = ['education_period', 'seats_amount']


class EnrolleeSpecialityAdmin(admin.ModelAdmin):
    list_display = [
        'enrollee',
        'speciality',
        'is_priority',
        'is_enrolled',
    ]
    search_fields = ['enrollee']
    list_filter = ['speciality', 'is_priority', 'is_enrolled']


class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'closing_date']
    search_fields = ['name']
    actions = ['close_recruitments', 'cancel_enrollment']

    @admin.action(description="Зачислить выбранные наборы")
    def close_recruitments(self, request, queryset):
        for recruitment in queryset:
            use_cases.enroll_recruitment(recruitment.name)
        self.message_user(
            request, 
            'Зачисление по выбранным наборов произведено успешно.',
        )

    @admin.action(description="Отменить зачисление")
    def cancel_enrollment(self, request, queryset):
        for recruitment in queryset:
            use_cases.cancel_enrollment(recruitment.name)
        self.message_user(
            request,
            'Отмена зачисления выбранных наборов произведено успешно.',
        )


admin.site.register(models.Enrollee, EnrolleeAdmin)
admin.site.register(models.Speciality, SpecialityAdmin)
admin.site.register(models.EnrolleeSpeciality, EnrolleeSpecialityAdmin)
admin.site.register(models.Recruitment, RecruitmentAdmin)

admin.site.site_header = 'ПКИПТ API'
admin.site.site_title = 'ПКИПТ API'
