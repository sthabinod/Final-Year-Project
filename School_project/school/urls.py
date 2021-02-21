from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views  as authview

urlpatterns = [
    path('',views.landing_page,name="landing_page"),
    path('about',views.about,name="about"),
    path('events',views.events,name="events"),
    path('event-details/<uuid>',views.event_details,name="event_details"),
    path('add-result',views.add_result,name="add_result"),
    path('view-result',views.view_result,name="view_result"),
    path('display-result',views.display_result,name="display_result"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)