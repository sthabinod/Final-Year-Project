# Generated by Django 3.1.5 on 2021-01-29 17:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_code', models.IntegerField(verbose_name='Address Code(Test)')),
                ('address_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Events Categories',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_created=True)),
                ('class_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ParentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, unique=True)),
                ('date_of_birth', models.DateField()),
                ('email_address', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('approved', models.BooleanField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.address')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(auto_created=True)),
                ('subject_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=200)),
                ('file', models.FileField(upload_to='')),
                ('profile_image', models.ImageField(upload_to='')),
                ('approved', models.BooleanField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.address')),
                ('related_class', models.ManyToManyField(to='school.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('email_address', models.EmailField(max_length=100, unique=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.address')),
                ('parent_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.parenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_year', models.DateField()),
                ('exam_date_time', models.DateTimeField(auto_now_add=True)),
                ('exam_term', models.CharField(choices=[('FT', 'First Term'), ('ST', 'Second Term'), ('TT', 'Third Term')], max_length=2)),
                ('exam_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.class')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('ids', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('featured_image', models.ImageField(null=True, upload_to='static/images/events_image')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('venue', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('tags', models.CharField(max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_edited', models.DateField()),
                ('featured', models.BooleanField()),
                ('block', models.BooleanField()),
                ('schedule', models.TimeField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.category')),
                ('student', models.ManyToManyField(to='school.Student')),
                ('teacher', models.ManyToManyField(to='school.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.subject')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.teacher')),
            ],
            options={
                'verbose_name_plural': 'Subject and Teacher',
                'unique_together': {('subject_code', 'teacher_id')},
            },
        ),
        migrations.CreateModel(
            name='SubjectMarksTeacherStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.DecimalField(decimal_places=2, max_digits=100)),
                ('student_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.student')),
                ('subject_number', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.subject')),
                ('teacher_code', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.teacher')),
            ],
            options={
                'verbose_name_plural': 'Kind of result',
                'unique_together': {('subject_number', 'teacher_code', 'student_code')},
            },
        ),
        migrations.CreateModel(
            name='StudentTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.student')),
                ('teachers_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.teacher')),
            ],
            options={
                'verbose_name_plural': 'Student and Teacher',
                'unique_together': {('students_id', 'teachers_id')},
            },
        ),
    ]
