from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 

# Create your views here.

monthly_challenges = {
    "january": "eat no meat for the entire month !",
    "february": "walk for at least 20 minutes a day !",
    "march": "learn django for 30 minutes each day !",
    "april": "apply for django jobs for entire month",
    "may": "play basketball 3- 4 times a week",
    "june": "play call of duty everyday",
    "july": "play in flag football league",
    "august": "spend a month in a different country",
    "september": "do some gardening every weekend",
    "october": "go fishing everyday",
    "november": "read a book everyday",
    "december": "go to the gym at least 5 times a week"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported !</h1>")