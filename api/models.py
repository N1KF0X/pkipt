from django.db import models


class Recruitment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название', primary_key=True)
    closing_date = models.DateField(verbose_name='Дата Закрытия Набора')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Набор'
        ordering = ['name', 'closing_date']


class Enrollee(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='ФИО')
    snils = models.CharField(primary_key=True, max_length=14, verbose_name='СНИЛС')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    gpa = models.FloatField(verbose_name='Средний Балл')
    application_date = models.DateField(verbose_name='Дата Подачи Документов')
    recruitment = models.ForeignKey(
        Recruitment, 
        on_delete = models.CASCADE, 
        verbose_name='Набор',
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриенты'
        ordering = ['full_name', 'inn', 'gpa', 'recruitment', 'application_date']


class Speciality(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', primary_key=True)
    seats_amount = models.IntegerField(verbose_name='Количество Мест', default=25)
    education_period = models.CharField(max_length=50, verbose_name='Срок Обучения') 
    code=models.CharField(max_length=8, verbose_name='Код')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ['name', 'code']


class EnrolleeSpeciality(models.Model):
    enrollee = models.ForeignKey(
        Enrollee, 
        on_delete = models.CASCADE, 
        verbose_name='Абитуриент',
        related_name='selected_specialities',
    )
    speciality = models.ForeignKey(
        Speciality, 
        on_delete = models.CASCADE, 
        verbose_name='Специальность',
    )
    is_priority = models.BooleanField(verbose_name='Приоритетная', default=False)
    is_enrolled = models.BooleanField(verbose_name='Зачислен', default=False)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Выбранная Специальность'
        verbose_name_plural = 'Выбранные Специальности'
        ordering = ['enrollee', 'speciality', 'is_priority']
