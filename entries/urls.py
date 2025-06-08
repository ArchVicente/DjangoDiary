from django.urls import path
from . import views
urlpatterns = [
    path(
        "", # URL pattern
        views.EntryListView.as_view(), # ListView for entries
        name="entry-list" # Name for referencing this URL
    ),
    path(
        "entry/<int:pk>",
        views.EntryDetailView.as_view(),
        name="entry-detail"
    ),
]