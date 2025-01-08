from django.contrib import admin  
from .models import Course, Note 
from .models import Payment

admin.site.register(Course)  
admin.site.register(Note)


from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'transaction_id', 'amount', 'is_confirmed', 'created_at')
    list_filter = ('is_confirmed', 'created_at')  # Replace 'timestamp' with 'created_at'
    search_fields = ('transaction_id', 'user__username', 'course__title')

admin.site.register(Payment, PaymentAdmin)


