from django.shortcuts import render
def show_main(request):
    context = {
        'name': 'rendra',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
