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

class library_management(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Media/')
    date_of_borrow = models.DateField(auto_now=True)
    date_of_return = models.DateField()
    
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='borrowed_books')
    class_name = models.CharField(max_length=100)  # Use same type as in Students model
    section = models.CharField(max_length=100)     # Use same type as in Students model

    def __str__(self):
        return self.book_name + " " + self.author

    