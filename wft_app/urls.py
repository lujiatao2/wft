from django.urls import path
from django.views.generic import RedirectView

from wft_app import views

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='static/img/favicon.ico')),
    path('', views.index),
    path('browser', views.browser),
    path('element', views.element),
    path('mouse-and-keyboard', views.mouse_and_keyboard),
    path('mouse-and-keyboard/<level_1_menu>/<level_2_menu>', views.specific_page),
    path('wait', views.wait),
    path('javascript', views.javascript),
    path('upload-and-download', views.upload_and_download)
]
