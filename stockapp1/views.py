from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def home( request):
    context = { 'username': 'Ian Wehmeyer'}
    return render( request, 'stockapp1/home.html', context)