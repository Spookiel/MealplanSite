from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def tracker_index(request):
    return render(request, "tracker/index.html")