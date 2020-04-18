from django.views import generic
from art_literature.models import Poetry, Story, Novel


#==========================================================

class PoetryListView(generic.ListView):
    model = Poetry
    paginate_by = 4



class PoetryDetailView(generic.DetailView):
    model = Poetry



#==========================================================

class StoryListView(generic.ListView):
    model = Story
    paginate_by = 4


class StoryDetailView(generic.DetailView):
    model = Story




#=====================================================

class NovelListView(generic.ListView):
    model = Novel
    paginate_by = 4



class NovelDetailView(generic.DetailView):
    model = Novel
