from django.contrib import admin
from .models import TrialRequest, Decision
# Register your models here.

@admin.register(TrialRequest)
class TrialRequestAdmin(admin.ModelAdmin):
    list_display=('requested_by', 'request_date', 'version',)
    search_fields=('requested_by__username','version__version_no','justification',)
    ordering=('-request_date',)

""" Why NOT put justification in list_display
TextField → long, ugly rows
Breaks table layout
 """

@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    list_display=('decided_by', 'comment', 'decision_date','trial', 'decision',)
    search_fields=('decided_by__username', 'decision','trial__version__version_no',)
    list_filter = ('decision',)
    ordering=('-decision_date',)

""" Why trial__version__version_no
Let’s walk it slowly:

Decision
 └── trial (OneToOne)
      └── version (ForeignKey)
           └── version_no (CharField)

So Django path becomes:
trial__version__version_no
This is ORM graph traversal, not magic. """


""" search_fields
Purpose	Free-text search
SQL	LIKE %value%
Best for	names, codes, messages
Bad for	dates, numbers, booleans
User experience	Search box """

""" list_filter
Purpose	Structured filtering
SQL	WHERE field = value
Best for	status, dates, booleans
UI	Sidebar """