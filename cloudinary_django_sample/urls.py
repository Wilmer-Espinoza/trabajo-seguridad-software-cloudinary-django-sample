from django.urls import re_path

from django.contrib import admin

admin.autodiscover()

import photo_album.views as photo_album

urlpatterns = [
    # URL for listing all images:
    re_path(r'^$', photo_album.list),
    re_path(r'^list$', photo_album.list, name='photo_album.views.list'),
    # URL for uploading an image
    re_path(r'^upload$', photo_album.upload, name='photo_album.views.upload'),
    # The direct upload functionality reports to this URL when an image is uploaded.
    re_path(r'^upload/complete$', photo_album.direct_upload_complete, name='photo_album.views.direct_upload_complete'),
    # Add the admin functionality:
    re_path(r'^admin/', admin.site.urls),
]
