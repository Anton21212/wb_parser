from django.urls import path

from core.views import WbApiView

app_name = 'core'

urlpatterns = [
    path('get_cards_info/', WbApiView.as_view()),
]
