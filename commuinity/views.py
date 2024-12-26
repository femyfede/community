from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Course
from .forms import PaymentForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'community/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Simulate payment processing
            course.is_paid = True
            course.save()
            return redirect('course_detail', pk=pk)  # Redirect to the course detail page
    else:
        form = PaymentForm()

    return render(request, 'community/payment.html', {'course': course, 'form': form})

def payment_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            payment_method = form.cleaned_data['payment_method']

            # Process payment here (You can integrate payment gateway APIs)
            if payment_method == 'phone':
                # Example: Store phone payment info
                print(f'Phone Payment Initiated. Phone: {phone_number}, Course: {course.title}')
            else:
                print(f'Card Payment Initiated for {course.title}')

            return redirect('payment_success')  # Redirect to success page
    else:
        form = PaymentForm()
    return render(request, 'community/payment.html', {'course': course, 'form': form})



