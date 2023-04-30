from django.shortcuts import render

# Create your views here.

def render_menu(request):
    """Render the menu from the implemented
    MenuItem class"""
    return render(template_name="menu.html", request=request)
