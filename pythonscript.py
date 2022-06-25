from django.shortcuts import render
import requests


def button(request):

    return render(request, simulation)


def output(request):
    data = requests.get('https://www.google.com/?client=safari')
    print(data)
    data = data.text
    return render(request, 'simulation.html', {'data':data})



print('\nStart script\n')

print('\n**End**')