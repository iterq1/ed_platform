from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=256)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'


class Lesson(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(default='text')
    order = models.PositiveSmallIntegerField(default=1)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.PROTECT)

    class Meta:
        ordering = ('course', 'order', )

    def __str__(self):
        return f'{self.title}'


class Building(models.Model):
    floors_number = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Theater(Building):
    pass


class School(Building):
    pass
