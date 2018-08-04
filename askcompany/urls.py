from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dialogflow/', include('dialogflow.urls')),
    path('plusfriend/', include('plusfriend.urls')),
    path('', RedirectView.as_view(pattern_name='dialogflow:index'), name='root'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
