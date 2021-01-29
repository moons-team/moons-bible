from django.contrib import admin
from thebible.models import BibleVersions, BibleTitles, BibleChapters, BibleVerses, KeywordsInfo
# Register your models here.
admin.site.register(BibleVersions)
admin.site.register(BibleTitles)
admin.site.register(BibleChapters)
admin.site.register(BibleVerses)
admin.site.register(KeywordsInfo)