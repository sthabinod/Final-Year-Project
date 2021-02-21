from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Event
from .decorators import allowed_users
from .models import Student, Teacher, SubjectMarksTeacherStudent, Subject


def landing_page(request):
    return render(request, 'school/index.html')


def about(request):
    return render(request, 'school/about.html')


def events(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})


@login_required(login_url='login')
def event_details(request, id):
    event = Event.objects.get(id=id)
    events = Event.objects.filter(id__range=(2, 3)).order_by("?")
    return render(request, 'events/event_details.html', {'event': event, 'events': events})


@login_required(login_url='login')
@allowed_users(allowed=['Admin', 'Teacher'])
def add_result(request):
    return render(request, 'result/add_result.html')


@login_required(login_url='login')
@allowed_users(allowed=['Admin', 'Student'])
def view_result(request):
    return render(request, 'result/view_result.html')


@login_required(login_url='login')
@allowed_users(allowed=['Admin', 'Student'])
def display_result(request):
    students = Student.objects.all().select_related(SubjectMarksTeacherStudent)
    for student in students:
        print(student.full_name)

    return render(request, 'result/display_result.html')
