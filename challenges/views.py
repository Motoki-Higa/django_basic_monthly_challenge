from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 mins everyday!',
    'march': 'Learn Django for at least 20 mins everyday!',
    'april': None
}

# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
      "months": months
    })


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
          "month_name": month,
        })
    except:
        return HttpResponseNotFound('<h1>This month is not supported!</h1>')
