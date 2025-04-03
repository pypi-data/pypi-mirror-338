from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.ListView.as_view(),
        name="notification-list",
    ),
    path(
        "mark-read/",
        views.MarkReadView.as_view(),
        name="notification-mark-read",
    ),
    path(
        "set-star/<str:uuid>/",
        views.SetStarView.as_view(),
        name="notification-set-star",
    ),
    path(
        "unread-count/",
        views.UnreadCountView.as_view(),
        name="notification-unread-count",
    ),
]
