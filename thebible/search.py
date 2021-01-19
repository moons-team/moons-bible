from haystack import indexes
from thebible.models import BibleVerses

class BibleVersesIndex(indexes.SearchIndex, indexes.Indexable):
    keyword = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return BibleVerses
    def index_queryset(self, using=None):
        return self.get_model().objects.all()