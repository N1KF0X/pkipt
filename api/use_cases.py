import datetime, typing

from django.core import exceptions

from . import exc, models


def get_enrollees_by_recruitment_name(recruitment_name: int) -> typing.List[models.Enrollee]:
    return models.Enrollee.objects.filter(recruitment=recruitment_name)


def get_selected_specialitiy_by_enrollee_snils(
    enrollee_snils: str,
    is_priority: bool = True,
) -> typing.Union[models.EnrolleeSpeciality, None]:
    return models.EnrolleeSpeciality.objects.filter(
        enrollee=enrollee_snils,
        is_priority=is_priority,
    ).first()


def get_enrollee(enrollee_snils: str):
    try:
        return models.Enrollee.objects.get(snils=enrollee_snils)
    except exceptions.ObjectDoesNotExist:
        raise exc.EnrolleeNotFound()


def get_selected_specialities_by_speciality(
    speciality_name: str,
    is_priority: bool = True,
) -> typing.List[models.EnrolleeSpeciality]:
    return models.EnrolleeSpeciality.objects.filter(
        speciality=speciality_name,
        is_priority=is_priority,
    )


def calculate_rating(enrollee_snils: str) -> int:
    current_enrollee = get_enrollee(enrollee_snils)
    selected_speciality = get_selected_specialitiy_by_enrollee_snils(
        enrollee_snils=enrollee_snils,
    )

    if selected_speciality is None:
        raise exc.EnrolleeDoesNotHavePrioritySpeciality()

    selected_specialities = get_selected_specialities_by_speciality(
        speciality_name=selected_speciality.speciality.name,
    )
    enrollee_snils = [
        selected_speciality.enrollee.snils
        for selected_speciality 
        in selected_specialities
    ]

    enrollees = models.Enrollee.objects.filter(
        recruitment=current_enrollee.recruitment,
        snils__in=enrollee_snils,
    ).order_by('-gpa', 'application_date')

    raiting = 0
    for enrollee in enrollees:
        raiting += 1
        if enrollee.snils == current_enrollee.snils:
            break         
    
    return raiting


def enroll_recruitment(recruitment_name: str):
    enrollees = get_enrollees_by_recruitment_name(recruitment_name)
    for enrollee in enrollees:
        priority_speciality = get_selected_specialitiy_by_enrollee_snils(enrollee.snils)
        if priority_speciality is None:
            continue
        if calculate_rating(enrollee.snils) <= priority_speciality.speciality.seats_amount:
            priority_speciality.is_enrolled = True
        else:
            priority_speciality.is_enrolled = False
        priority_speciality.save()


def cancel_enrollment(recruitment_name: str):
    enrollees = get_enrollees_by_recruitment_name(recruitment_name)
    for enrollee in enrollees:
        priority_speciality = get_selected_specialitiy_by_enrollee_snils(enrollee.snils)
        if priority_speciality is None:
            continue
        priority_speciality.is_enrolled = False
        priority_speciality.save()


def get_recruitments() -> typing.List[models.Recruitment]:
    return models.Recruitment.objects.filter(
        closing_date__gt=datetime.datetime.now()
    )


def get_specialities():
    return models.Speciality.objects.all()
