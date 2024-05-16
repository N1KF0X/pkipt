from rest_framework.exceptions import APIException


class EnrolleNotFound(APIException):
    status_code = 404
    default_detail = 'Абитуриент с данным СНИСЛ не найден.'
    default_code = 'абитуриент не найден'


class EnrolleeDoesNotHavePrioritySpeciality(APIException):
    status_code = 400
    default_detail = 'Абитуриент не имеет приоритетной специальности.'
    default_code = 'нет приоритетной специальности'
