from django.shortcuts import render
from django.views import generic  # 2nd
#from catalog.serializers import NationSerializer, InternationalSerializer, SportSerializer, EntertainmentSerializer, LifestyleSerializer
from international.models import Subcontinent, Asia, MiddleEast, UnitedState, Europe, InternationalOrganization


#==========================================================

class SubcontinentListView(generic.ListView):
    model = Subcontinent
    paginate_by = 4



class SubcontinentDetailView(generic.DetailView):
    model = Subcontinent



#==========================================================

class AsiaListView(generic.ListView):
    model = Asia
    paginate_by = 4


class AsiaDetailView(generic.DetailView):
    model = Asia




#=====================================================

class MiddleEastListView(generic.ListView):
    model = MiddleEast
    paginate_by = 4



class MiddleEastDetailView(generic.DetailView):
    model = MiddleEast




#=======================================================

class UnitedStateListView(generic.ListView):
    model = UnitedState
    paginate_by = 4


class UnitedStateDetailView(generic.DetailView):
    model = UnitedState


#===========================================

class EuropeListView(generic.ListView):
    model = Europe
    paginate_by = 4



class EuropeDetailView(generic.DetailView):
    model = Europe





#=======================================================

class InternationalOrganizationListView(generic.ListView):
    model = InternationalOrganization
    paginate_by = 2


class InternationalOrganizationDetailView(generic.DetailView):
    model = InternationalOrganization

