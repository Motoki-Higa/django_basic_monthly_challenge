from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 mins everyday!',
    'march': 'Learn Django for at least 20 mins everyday!'
}

# Create your views here.
def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
      capitalized_month = month.capitalize()
      month_path = reverse('month-challenge', args=[month])
      list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month] # this 'month' should be same as the identifier you set in urls.py
        return render(request, "challenges/challenge.html", {
          "text":  challenge_text,
          "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
