from django.db import models
from Subject.models import Subject
from Student.models import Student

# Create your models here.
class PointSj(models.Model):
    student_id = models.ForeignKey(Student, default = None, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, default = None, on_delete = models.CASCADE)
    pointsj_dcc = models.FloatField(null = True)
    pointsj_exam = models.FloatField(null = True)

     
    @property
    def average_grade(self):
        return (self.pointsj_dcc + self.pointsj_exam) / 2

    @property
    def grade_pointsj(self):
        if self.average_grade >= 9:
            return 4.0
        elif self.average_grade >= 8:
            return 3.5
        elif self.average_grade >= 7:
            return 3.0
        elif self.average_grade >= 6:
            return 2.5
        elif self.average_grade >= 5:
            return 2.0
        elif self.average_grade >= 4:
            return 1.5
        elif self.average_grade >= 3:
            return 1.0
        else:
            return 0.0
        
    def __str__(self):
        return f"{self.student_id},{self.subject_id},{self.pointsj_dcc},{self.pointsj_exam},{self.average_grade},{self.grade_pointsj}"
    class Meta:
        unique_together = ('student_id', 'subject_id')