from django.conf.urls import url
from support import views

app_name = 'support'

urlpatterns = [
    url(r'^support_form/$',
            views.Contact_Us,
            name='support'),

]
