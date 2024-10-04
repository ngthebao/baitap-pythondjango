from django.db import models



# Create your models here.
class Student(models.Model):
    std_id = models.AutoField(primary_key=True)
    std_msv = models.CharField(max_length=191)
    std_name = models.CharField(max_length=20)
    std_year = models.DateField("Ngày sinh")
    std_address = models.CharField(max_length=191)
    std_gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.std_id},{self.std_msv},{self.std_name},{self.std_year},{self.std_address},{self.std_gender}"
    