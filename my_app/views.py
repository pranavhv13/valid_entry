from django.apps import apps
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Event, FormConfig
from .forms import create_dynamic_form

def index(request):
    # return HttpResponse("This is a function based view.")
    context = {
        'key' : 'value'
    }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def events(request):
    upcoming_events = Event.objects.filter(isDone=False).order_by('date')
    completed_events = Event.objects.filter(isDone=True).order_by('-date')
    return render(request, 'events.html', {
        'upcoming_events': upcoming_events,
        'completed_events': completed_events,
    })

def event_info(request, event_id):
    event = Event.objects.get(id=event_id) 
    return render(request, 'event_info.html', {'event': event})

def sucess(request):
    return render(request, 'sucess.html')

def register_event(request, event_id, form_id):
    # Fetch the event and form configuration
    event = get_object_or_404(Event, id=event_id)
    form_config = get_object_or_404(FormConfig, id=form_id)
    FORM_CONFIGS = form_config.fields  

    # Create the dynamic form
    DynamicForm = create_dynamic_form(form_id)

    if request.method == 'POST':
        form = DynamicForm(request.POST, request.FILES) 
        if form.is_valid():
            # Handle the form submission
            submitted_data = form.cleaned_data
            print(submitted_data)  
            # Dynamically create an instance of the Ticket model based on form_id
            ticket_class_name = f'ticket_{form_id}'  # Assuming your model class names are ticket_1, ticket_2, etc.
            
            try:
                TicketClass = apps.get_model('my_app', ticket_class_name)  # Replace 'my_app' with your app name
            except LookupError:
                # Handle the case where the model class does not exist
                return HttpResponse("Ticket model not found.")
            
            # Create a new Ticket instance
            ticket = TicketClass(event=event)

            for field_name, value in submitted_data.items():
                setattr(ticket, field_name, value)  # Set dynamic fields
            
            ticket.save()  # Save the ticket to the database
            
            # Optionally, you can also pass the submitted data to the success template
            return render(request, 'sucess.html', {'submitted_data': submitted_data})

    else:
        form = DynamicForm()  # Initialize the form for GET requests

    return render(request, 'register_event.html', 
                  {'event': event, 
                   'form': form, 'title': FORM_CONFIGS['title'], 
                   'form_id': form_id,
                   'event_form_id': event.form_id })