from django.urls import re_path
from api.views import UserView, loginView, recordView, paymentView

urlpatterns = [
    re_path(r'^login$', loginView.as_view()),
    re_path(r'^user$', UserView.as_view()),
    re_path(r'^user/([0-9]+)$', UserView.as_view()),
    re_path(r'^record$', recordView.as_view()),
    re_path(r'^record/([0-9]+)$', recordView.as_view()),
    re_path(r'^payments/$', paymentView.as_view()),
]
