from django.shortcuts import redirect, render
from crud_app.forms import PersonForm
from crud_app.models import Person
from django.core.paginator import Paginator

# Create your views here.

# this view contains the logic for the home page
def home(request):
    data={}
    #data['db'] = Person.objects.all
    all = Person.objects.all()
    paginator = Paginator(all, 3)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

# this view contains the logic for the form page
def form(request):
    data = {}
    data[form] = PersonForm()
    return render(request, 'form.html', data)

# this view contains the logic for the create page
def create(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('home')

# this view contains the logic for the update page
def edit(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    data['form'] = PersonForm(instance=data['db'])
    return render(request, 'form.html', data)

# this view contains the logic for the update page
def update(request, pk):
    data = {}
    data['db'] = Person.objects.get(pk=pk)
    form = PersonForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'index.html')

# this view contains the logic for the delete page
def delete(request, pk):
    db = Person.objects.get(pk=pk)
    db.delete()
    return redirect('home')