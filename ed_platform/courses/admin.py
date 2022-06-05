from django.contrib import admin

from .models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', )
    search_fields = ('title', )
    list_filter = ('title', )
    empty_value_display = '-пусто-'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'order')
    search_fields = ('title', )
    list_filter = ('course', )
    empty_value_display = '-пусто-'
