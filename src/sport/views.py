from django.views import generic  # 2nd
from sport.models import Cricket, Football, Tennis, Swimming, Hockey


#==========================================================

class CricketListView(generic.ListView):
    model = Cricket
    paginate_by = 2



class CricketDetailView(generic.DetailView):
    model = Cricket



#==========================================================

class FootballListView(generic.ListView):
    model = Football
    paginate_by = 2


class FootballDetailView(generic.DetailView):
    model = Football




#=====================================================

class TennisListView(generic.ListView):
    model = Tennis
    paginate_by = 2



class TennisDetailView(generic.DetailView):
    model = Tennis




#=======================================================

class SwimmingListView(generic.ListView):
    model = Swimming
    paginate_by = 2


class SwimmingDetailView(generic.DetailView):
    model = Swimming


#===========================================

class HockeyListView(generic.ListView):
    model = Hockey
    paginate_by = 2



class HockeyDetailView(generic.DetailView):
    model = Hockey

