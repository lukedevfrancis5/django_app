from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string


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
    "december": None
}

def index(request):
    
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
    # up top function shows what it will look like on client side 
    # "<li><a href="...">January</a></li><li><a href="..."February</a></li>
    

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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text, 
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)