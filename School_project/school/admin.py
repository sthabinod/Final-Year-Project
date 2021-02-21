from django.contrib import admin
from .models import Address, ParentType, Parent, Student, Category, Exam, Teacher, Event, Subject, Class, SubjectMarksTeacherStudent


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ('address_code','address_name')



@admin.register(ParentType)
class ParentTypeAdmin(admin.ModelAdmin):
    fields = ('type','date_created')
    # exclude =



@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    fields = ('full_name','parent_type','phone_number','email_address','addresss')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(SubjectMarksTeacherStudent)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['subject_number', 'teacher_code', 'student_code','mark']

