from django.shortcuts import render

# Create your views here.
def welcome_page(request):

	return render(request, "MyApp/welcome_page.html")