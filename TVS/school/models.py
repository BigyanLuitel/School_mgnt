from django.db import models

# Create your models here.
class Students(models.Model):
    student_id= models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    class_name=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    contact=models.IntegerField()
    parents=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    date_of_admission=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    class Meta:
        ordering = ['student_id']

class library_records(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    Edition=models.DateField()
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.book_name + " " + self.author


class library_Management(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(library_records, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=True)
    return_date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student.first_name + " " + self.book.book_name