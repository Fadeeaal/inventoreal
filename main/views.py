from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rakha Fadil Atmojo',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)