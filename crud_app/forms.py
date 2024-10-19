from django.forms import ModelForm
from crud_app.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'email', 'phone', 'address']