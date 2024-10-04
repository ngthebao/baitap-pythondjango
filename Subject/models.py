from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_msj = models.CharField(max_length = 50)
    subject_name = models.CharField(max_length = 50,null = False)
    subject_tc = models.IntegerField(null = True)

    def __str__(self):
        return f"{self.subject_id},{self.subject_msj},{self.subject_name},{self.subject_tc}"
