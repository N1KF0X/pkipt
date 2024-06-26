# Generated by Django 4.1.4 on 2024-05-16 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollee',
            fields=[
                ('full_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('snils', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='СНИЛС')),
                ('inn', models.CharField(max_length=12, verbose_name='ИНН')),
                ('gpa', models.FloatField(verbose_name='Средний Балл')),
                ('application_date', models.DateField(verbose_name='Дата Подачи Документов')),
            ],
            options={
                'verbose_name': 'Абитуриент',
                'verbose_name_plural': 'Абитуриенты',
                'ordering': ['full_name', 'inn', 'gpa', 'recruitment', 'application_date'],
            },
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Название')),
                ('closing_date', models.DateField(verbose_name='Дата Закрытия Набора')),
            ],
            options={
                'verbose_name': 'Набор',
                'verbose_name_plural': 'Набор',
                'ordering': ['name', 'closing_date'],
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Название')),
                ('seats_amount', models.IntegerField(default=25, verbose_name='Количество Мест')),
                ('education_period', models.CharField(max_length=50, verbose_name='Срок Обучения')),
                ('code', models.CharField(max_length=8, verbose_name='Код')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
                'ordering': ['name', 'code'],
            },
        ),
        migrations.CreateModel(
            name='EnrolleeSpeciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_priority', models.BooleanField(default=False, verbose_name='Приоритетная')),
                ('is_enrolled', models.BooleanField(default=False, verbose_name='Зачислен')),
                ('enrollee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_specialities', to='api.enrollee', verbose_name='Абитуриент')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.speciality', verbose_name='Специальность')),
            ],
            options={
                'verbose_name': 'Выбранная Специальность',
                'verbose_name_plural': 'Выбранные Специальности',
                'ordering': ['enrollee', 'speciality', 'is_priority'],
            },
        ),
        migrations.AddField(
            model_name='enrollee',
            name='recruitment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.recruitment', verbose_name='Набор'),
        ),
    ]
