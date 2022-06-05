from django.shortcuts import render, get_object_or_404

from courses.models import Course, Lesson


def index(request):
    courses = Course.objects.filter(visible=True)
    context = {
        'courses': courses
    }
    return render(request, 'courses/index.html', context)


def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    context = {
        'course': course
    }
    return render(request, 'courses/course_details.html', context)


def lesson_details(request, course_id, lesson_id):
    lesson = Lesson.objects.select_related('course').filter(course_id=course_id, id=lesson_id).first()
    print(lesson, lesson.course)
    context = {
        'lesson': lesson
    }
    return render(request, 'courses/lesson.html', context)
