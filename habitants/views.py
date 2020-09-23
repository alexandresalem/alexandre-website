from django.shortcuts import render
from django.http import HttpResponse
from .habitants import world_data, play, us_data

# Create your views here.
def habitants(request):
    context = {}
    context['placeholder'] = "Write some number..."
    context['display'] = 'hidden'
    return render(request, 'habitants/home.html', context)

def result(request):
    val1 = request.GET['num1']
    game = request.GET['game-option']
    try:
        val1 = int(val1)
        if val1 <= 0:
            return render(request, 'habitants/home.html', {'placeholder': 'Number must be higher then zero!','display':'visible'})
        elif val1 > 7800000000:
            return render(request, 'habitants/home.html',{'placeholder': "World's population is around 7.8 billion. Please try a smaller number.", 'display': 'visible'})
    except:
        return render(request, 'habitants/home.html', {'placeholder':'That was not a valid number!','display':'visible'})


    population, country, ranking, flag, city_pop, city_name, city_state, city_ranking = play(world_data(),us_data(),val1)

    context = {}
    context['pop'] = val1
    context['population'] = population
    context['country'] = country
    context['ranking'] = int(ranking)+1
    context['flag'] = flag
    context['city_pop'] = city_pop
    context['city_name'] = city_name
    context['city_state'] = city_state
    context['city_ranking'] = city_ranking+1

    # Check which option the player selected
    if game != '2':
        context['display_countries'] = 'block'
        if game == '3':
            context['display_cities'] = 'block'
        elif game == 'Countries or US Cities?':
            return render(request, 'habitants/home.html', {'placeholder': 'Choose between countries or US cities!'})
        else:
            context['display_cities'] = 'none'
    elif game =='2':
        context['display_countries'] = 'none'
        context['display_cities'] = 'block'




    return render(request, 'habitants/prediction.html', context)