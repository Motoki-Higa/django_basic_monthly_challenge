from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

monthly_challenges = {
  'january': 'Eat no meat for the entire month',
  'february': 'Walk for at least 20 mins everyday!',
  'march': 'Learn Django for at least 20 mins everyday!'
}
# Create your views here.


# this 'month' should be same as the identifier you set in urls.py
def monthly_challenge(request, month):
    try:
      challenge_text = monthly_challenges[month]
      return HttpResponse(challenge_text)
    except: 
      return HttpResponseNotFound('This month is not supported!')
    
