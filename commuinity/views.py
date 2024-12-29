from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .models import Course
from .forms import PaymentForm
from django.urls import reverse


def payment_success(request):
    return render(request, 'community/payment_success.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'community/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            course.is_paid = True
            course.save()
            return redirect('course_detail', pk=pk)  
    else:
        form = PaymentForm()

    return render(request, 'community/payment.html', {'course': course, 'form': form})


def payment_view(request, pk):

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":


        form = PaymentForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            payment_method = form.cleaned_data['payment_method']
            
            payment_success =  course.is_paid = True
            course.save()

            if payment_success:
                return redirect('payment_success')  # Redirect to success page
            else:
                return HttpResponse("Payment Failed. Please try again.")

            return redirect('payment_success')  
        
        # continue_payment method, but make sure the payment logic is working properly defined --- Good luck with it [ lemajr ]


    else:
        form = PaymentForm()
    return render(request, 'community/payment.html', {'form': form, 'course': course})
