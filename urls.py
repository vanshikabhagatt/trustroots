from django.urls import path
from grassroots import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "grassroot_app"

urlpatterns = [
    path("search-grassroot/", views.search_grassroot, name="search-grassroot"),
    path("follow-grassroot/<int:grassroot_id>", views.follow_grassroot, name="follow-grassroot"),
    path("unfollow-grassroot/<int:id>", views.unfollow_grassroot, name="unfollow-grassroot")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
