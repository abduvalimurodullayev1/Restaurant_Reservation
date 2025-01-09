from apps.reservation.views import *
from django.urls import path    

app_name = "reservation"

urlpatterns = [
    path("", ReservationListView.as_view(), name="list"),
    path("create/", ReservationApiView.as_view(), name="create"),
    path("<int:pk>/delete/", ReservationDelete.as_view(), name="delete"),        
    path("<int:pk>/update/", ReservationUpdate.as_view(), name="update"),   
    
]
