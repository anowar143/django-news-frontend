from django.views import generic  # 2nd
from other.models import Ramadan, Feature


#==========================================================

class RamadanListView(generic.ListView):
    model = Ramadan
    paginate_by = 4



class RamadanDetailView(generic.DetailView):
    model = Ramadan



#==========================================================

class FeatureListView(generic.ListView):
    model = Feature
    paginate_by = 2


class FeatureDetailView(generic.DetailView):
    model = Feature



