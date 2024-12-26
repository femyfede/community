from django.db import models

class Note(models.Model):
    course = models.ForeignKey('commuinity.Course', related_name='notes', on_delete=models.CASCADE)  # String reference
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Payment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # New phone number field
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course.title}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price field

    def __str__(self):
        return self.title
