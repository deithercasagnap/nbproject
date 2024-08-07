from django.shortcuts import render
from django.http import HttpResponse
from myapp.functions import handle_uploaded_file
from myapp.forms import ProductForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        product = ProductForm(request.POST, request.FILES)
        if product.is_valid():
            handle_uploaded_file(request.FILES['file'])
            model_instance = product.save(commit=False)
            model_instance.save()
            return HttpResponse("File uploaded successfully!")

    else:
        product = ProductForm()
        return render(request, "index.html", {'form':product})






