from django.shortcuts import render

# Create your views here.
from .models import Holiday

# Vue pour les jours fériés
def holiday_list(request):
    holidays = Holiday.objects.all() # Récupère tous les jours fériés
    return render(request, 'planning/holidays.html', {'holidays': holidays})

# Vue pour l'emploi du temps (Bonus 5 points)
def timetable_view(request):
    return render(request, 'planning/timetable.html')