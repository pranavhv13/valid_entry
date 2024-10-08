from django.db import models
from django.db.models import JSONField

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    isDone = models.BooleanField(default=False) # True for completed, False for upcoming
    location = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='banners/',blank= True, null= True)
    poster = models.ImageField(upload_to='posters/',blank= True, null= True)
    more_info = models.TextField(blank= True, null= True)
    form_id = models.IntegerField(blank= True, null= True)

    def __str__(self):
        return self.title


class FormConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20,blank= True, null= True)
    fields = JSONField()  # Store form fields as JSON data
    
    def __str__(self):
        return self.title
    
class ticket_3(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,null= True)
    first_name = models.CharField(max_length=100,blank= True, null= True)  
    last_name = models.CharField(max_length=100,blank= True, null= True)  
    
    
# class Ticket(models.Model):
#     ticket_id = models.AutoField(primary_key=True)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Foreign key to Event

#     class Meta:
#         app_label = 'my_app'  # Replace with your actual app name

#     @classmethod
#     def create_dynamic_ticket_model(cls, form_id):
#         form_config = FormConfig.objects.get(id=form_id)
#         config = form_config.fields
#         field_data = config.get('fields', [])

#         for field in field_data:
#             field_type = field['type']
#             field_name = field['name']
#             if field_type == 'text':
#                 cls.add_to_class(field_name, models.CharField(max_length=255))
#             elif field_type == 'email':
#                 cls.add_to_class(field_name, models.EmailField())
#             elif field_type == 'textarea':
#                 cls.add_to_class(field_name, models.TextField())
#             elif field_type == 'number':
#                 cls.add_to_class(field_name, models.IntegerField())
#             elif field_type == 'image':
#                 cls.add_to_class(field_name, models.ImageField(upload_to='tickets/'))  # Adjust upload_to as needed

#         return cls
    
# from django.db import models

# class BaseDynamicModel(models.Model):
#     class Meta:
#         abstract = True

    
# def create_dynamic_model(form_id):
#     # Fetch form configuration
#     form_config = FormConfig.objects.get(id=form_id)
#     fields = form_config.fields.get('fields', [])

#     # Prepare the fields for the model
#     attrs = {}
    
#     attrs[ticket_id] = models.AutoField(primary_key=True)
#     attrs[form_id] = models.ForeignKey(Form, on_delete=models.CASCADE) 
#     attrs[event_id] = models.ForeignKey(Event, on_delete=models.CASCADE) 
#      # Foreign key to Event
#     for field in fields:
#         field_type = field['type']
#         field_name = field['name']
        
#         if field_type == 'text':
#             attrs[field_name] = models.CharField(max_length=255)
#         elif field_type == 'email':
#             attrs[field_name] = models.EmailField()
#         elif field_type == 'textarea':
#             attrs[field_name] = models.TextField()
#         elif field_type == 'number':
#             attrs[field_name] = models.IntegerField()
#         # Add more field types as needed

#     # Create the dynamic model
#     DynamicModel = type('DynamicModel', (BaseDynamicModel,), attrs)
#     return DynamicModel
