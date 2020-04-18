from django.views import generic  # 2nd
from national.models import Politic, Crime, Administration, Parliament, Economic, Education, Weather



#==========================================================

class PoliticListView(generic.ListView):
    model = Politic
    paginate_by = 2



class PoliticDetailView(generic.DetailView):
    model = Politic



#==========================================================

class CrimeListView(generic.ListView):
    model = Crime
    paginate_by = 2


class CrimeDetailView(generic.DetailView):
    model = Crime




#=====================================================

class AdministrationListView(generic.ListView):
    model = Administration
    paginate_by = 2



class AdministrationDetailView(generic.DetailView):
    model = Administration




#=======================================================

class ParliamentListView(generic.ListView):
    model = Parliament
    paginate_by = 2


class ParliamentDetailView(generic.DetailView):
    model = Parliament


#===========================================

class EconomicListView(generic.ListView):
    model = Economic
    paginate_by = 2



class EconomicDetailView(generic.DetailView):
    model = Economic


#=======================================================

class EducationListView(generic.ListView):
    model = Education
    paginate_by = 2


class EducationDetailView(generic.DetailView):
    model = Education


#===========================================

class WeatherListView(generic.ListView):
    model = Weather
    paginate_by = 2



class WeatherDetailView(generic.DetailView):
    model = Weather


