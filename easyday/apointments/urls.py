from django.urls import path
from apointments import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('create-appointment', views.AppointmentCreateView.as_view(), name='create_appointment'),
    path('list-appointment', views.AppoiuntmentListView.as_view(), name='list_appointment'),
    path('add-client', views.AddClient, name='add_client'),
    path('add-service', views.AddService, name='add_service'),
    path('delete-appointment/<int:pk>/', views.AppointmentDeleteView.as_view(), name='delete_appointment')


]
