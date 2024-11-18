from forms import views
from django.urls import path

urlpatterns = [
    path('',views.home ,name='home'),
    path('store',views.store ,name='store'),
    path('export',views.export ,name='export')
]
