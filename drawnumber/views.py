from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    context = {}
    # if request.method == 'POST':
    #     form = NumberForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #
    # form = NumberForm()
    #
    # context['form'] = form

    return render(request, 'drawnumber/home.html')

