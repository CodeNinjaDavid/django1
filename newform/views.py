from django.shortcuts import render
from newform.form import Names

def Home(request):
    jina = Names()
    return render(request, 'index.html', {'form':jina})