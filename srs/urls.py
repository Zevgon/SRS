from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('review.urls')),

]

# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # NOQA
