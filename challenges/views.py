from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

monthly_challenges = {
    'january': 'Eat no meat for the entire month',
    'february': 'Walk for at least 20 mins everyday!',
    'march': 'Learn Django for at least 20 mins everyday!'
}


# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect('/challenges/' + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month] # this 'month' should be same as the identifier you set in urls.py
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')
