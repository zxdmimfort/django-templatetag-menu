from django.shortcuts import render


def menu_view(request, menu_url=None):
    return render(request, "tabs/index.html", {"menu_url": menu_url})
