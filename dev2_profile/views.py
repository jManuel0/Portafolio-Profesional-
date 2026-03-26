from django.shortcuts import render


def index(request):
    """Render the Developer 2 curriculum vitae page."""
    return render(request, 'dev2_profile/index.html')
