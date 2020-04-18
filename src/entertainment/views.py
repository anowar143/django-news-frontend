from django.views import generic  #

from entertainment.models import Movie, Drama, Music


#==========================================================

class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 4



class MovieDetailView(generic.DetailView):
    model = Movie



#==========================================================

class DramaListView(generic.ListView):
    model = Drama
    paginate_by = 4


class DramaDetailView(generic.DetailView):
    model = Drama




#=====================================================

class MusicListView(generic.ListView):
    model = Music
    paginate_by = 4



class MusicDetailView(generic.DetailView):
    model = Music
