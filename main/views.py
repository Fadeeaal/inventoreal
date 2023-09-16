from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'creator': 'Rakha Fadil Atmojo',
        'pbpclass': 'PBP C'
    }

    return render(request, "main.html", context)