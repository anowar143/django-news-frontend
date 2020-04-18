from django.views import generic  # 2nd
from lifestyle.models import Health, Fashion, Cook


#==========================================================

class HealthListView(generic.ListView):
    model = Health
    paginate_by = 2



class HealthDetailView(generic.DetailView):
    model = Health



#==========================================================

class FashionListView(generic.ListView):
    model = Fashion
    paginate_by = 2


class FashionDetailView(generic.DetailView):
    model = Fashion




#=====================================================

class CookListView(generic.ListView):
    model = Cook
    paginate_by = 2



class CookDetailView(generic.DetailView):
    model = Cook



