from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .forms import PaymentForm
from django.urls import reverse
from .models import UserCourse, Course, Payment
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def study_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Check if the user has paid
    user_course = UserCourse.objects.filter(user=request.user, course=course).first()

    if not user_course or not user_course.is_paid:
        return HttpResponseForbidden("You have not paid for this course. Please make a payment.")

    if not user_course.payment_confirmed:  # Payment not confirmed by admin
        return HttpResponseForbidden("Payment is pending approval by admin. Please wait.")

    # If payment is confirmed
    return render(request, 'study_course.html', {'course': course})



def course_list(request):
    courses = Course.objects.all()  # Update model name
    return render(request, 'community/course_list.html', {'courses': courses})


@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, id=pk)
    payment = Payment.objects.filter(user=request.user, course=course, is_confirmed=True).exists()

    if not payment:
        return HttpResponseForbidden("Payment not confirmed. Please contact admin.")

    return render(request, 'community/course_detail.html', {'course': course})
def payment_success(request, course_id=None):
    if course_id:
        course = course.objects.get(id=course_id)
        UserCourse.objects.update_or_create(
            user=request.user, course=course, defaults={'is_paid': True}
        )
        return redirect('community/study_course', course_id=course_id)

    return render(request, 'community/payment_success.html')

@login_required
def payment_view(request, pk):
    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)  # Create a Payment instance but don't save yet
            payment.user = request.user  # Assign the user
            payment.course = course  # Assign the course
            payment.amount = course.price  # Use the course price
            payment.save()  # Save the Payment instance
            messages.success(request, "Payment submitted. Please wait for admin confirmation.")
            return redirect('course_list')  # Redirect after successful payment
    else:
        form = PaymentForm()

    return render(request, 'community/payment.html', {'course': course, 'form': form})


