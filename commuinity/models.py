from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)  # Tracks payment status
    payment_confirmed = models.BooleanField(default=False)  # Admin confirms payment
    created_at = models.DateTimeField(auto_now_add=True)


class Note(models.Model):
    # Corrected ForeignKey reference
    course = models.ForeignKey(Course, related_name='notes', on_delete=models.CASCADE)  
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Fixed reference
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)  # Added this field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title} - {self.transaction_id}"
