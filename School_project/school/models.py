import uuid

from django.db import models



class Address(models.Model):
    address_code = models.IntegerField(verbose_name="Address Code(Test)")
    address_name = models.CharField(max_length=200)

    def __str__(self):
        return self.address_name

    class Meta:
        verbose_name_plural = "Addresses"


# class Mark(models.Model):
#     achieved_mark = models.DecimalField(max_digits=20, null=False, blank=False, decimal_places=10)
#     marked_date = models.DateTimeField(auto_created=True, auto_now_add=True)
#
#     def __str__(self):
#         return "Marks"
#     #
    # def get_absolute_url(self):
    #     return reversed('school.views.')


class ParentType(models.Model):
    type = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type[:50]


class Parent(models.Model):
    full_name = models.CharField(max_length=255)
    parent_type = models.ForeignKey(ParentType, on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=11, blank=False, unique=True)
    email_address = models.EmailField(max_length=100, unique=True)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.full_name[:50]


class Student(models.Model):
    full_name = models.CharField(max_length=255,unique=True)
    date_of_birth = models.DateField(blank=False)
    email_address = models.EmailField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    approved = models.BooleanField()
    #
    # def age_validation(self):
    #     if self.age < 13:
    #         return "You are not qualified to register. Our school has children from class six only."

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.age<13:
            return
        else:
            super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]

    class Meta:
        verbose_name_plural ="Events Categories"


class Class(models.Model):
    class_name = models.CharField(max_length=20)
    registration_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.class_name


class Exam(models.Model):
    exam_year = models.DateField()
    exam_date_time = models.DateTimeField(auto_now_add=True)
    EXAM_TERM = [
        ('FT', 'First Term'),
        ('ST', 'Second Term'),
        ('TT', 'Third Term'),
    ]
    exam_term = models.CharField(max_length=2, choices=EXAM_TERM)
    exam_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Exam: " + self.exam_year


class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    file = models.FileField()
    profile_image = models.ImageField()
    related_class = models.ManyToManyField(Class)
    approved = models.BooleanField()

    def __str__(self):
        return self.full_name


class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    title = models.CharField(max_length=255)
    # slug = models.SlugField()
    featured_image = models.ImageField(null=True, upload_to='static/images/events_image')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    tags = models.CharField(max_length=100)
    teacher = models.ManyToManyField(Teacher)
    student = models.ManyToManyField(Student)
    date_added = models.DateField(auto_now_add=True)
    date_edited = models.DateField()
    featured = models.BooleanField()
    block = models.BooleanField()
    schedule = models.TimeField(max_length=100)

    def __str__(self):
        return self.title[:50]


class StudentTeacher(models.Model):
    students_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    teachers_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('students_id', 'teachers_id')
        verbose_name_plural = "Student and Teacher"

    def __str__(self):
        self.achieved_mark = "Tech Stu"


class Subject(models.Model):
    subject_code = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.subject_code


class SubjectTeacher(models.Model):
    subject_code = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('subject_code', 'teacher_id')
        verbose_name_plural = "Subject and Teacher"


class SubjectMarksTeacherStudent(models.Model):
    subject_number = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    teacher_code = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    student_code = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    mark = models.DecimalField(decimal_places=2, max_digits=100)

    class Meta:
        unique_together = ('subject_number', 'teacher_code', 'student_code')
        verbose_name_plural = "Kind of result"
