from django.db import models

# Create your models here.

class Course(models.Model):

    course_id = models.AutoField(primary_key = True)
    course_title = models.CharField(max_length = 30)
    course_description = models.CharField(max_length = 50)
    credit = models.IntegerField()
    instructor = models.CharField(max_length = 30)
    start_date = models.DateField()

    def __str__(self):
        return self.course_title