# Django
from django.shortcuts import render

def main(request):
    return render(request, 'users/base.html')