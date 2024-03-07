from django.shortcuts import render
from .models import Event
# Create your views here.
# def home(request):
#     obj=Event.objects.all()
#     ctx={"Events":obj}
#     return render(request,"event_management/index.html",ctx)

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import JsonResponse

def dashboard(request):
    if request.method == 'POST':
        # Handle the form submission for updating payment status
        event_ids = request.POST.getlist('event_ids')
        
        for event_id in event_ids:
            try:
                event = Event.objects.get(id=event_id)
                payment_status_key = f'payment_status_{event_id}'
                # print("POST DATA")
                # print("------------------------------------------")
                # print(request.POST)
                payment_status = int(request.POST.get(payment_status_key, 0))
                
                # Handle the attached bill
                bill_key = f'bill_{event_id}'
                attached_bill = request.FILES.get(bill_key)

                if payment_status == 1 and not attached_bill:
                    raise ValidationError("You must attach a bill for paid events")

                # Update the payment status
                event.payment_status = payment_status

                if attached_bill:
                    # Save the attached bill to the event
                    event.bill = attached_bill

                event.save()

            except Event.DoesNotExist:
                # Handle the case where the event with the given ID is not found
                pass

        # Redirect to the home page after processing the form submission
        return redirect('main:home')

    else:
        # Render the initial page with events
        obj = Event.objects.all()
        ctx = {"Events": obj}
        return render(request, "event_management/index.html", ctx)
