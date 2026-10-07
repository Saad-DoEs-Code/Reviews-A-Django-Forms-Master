from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm


# Create your views here.
def reviews(req):

    if req.method == "POST":
        form = ReviewForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_name = form.cleaned_data["username"]
            print(f"User Name is {user_name}")
            return HttpResponseRedirect("/thank-you")
    
    else:
        form = ReviewForm()
    return render(req, "reviews/review.html", {"form": form})


def thank_you(req):

    return render(req, "reviews/thanks.html")
