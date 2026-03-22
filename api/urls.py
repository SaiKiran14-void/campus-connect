from django.urls import path
from . import views

urlpatterns =[
path('signup/', views.signup, name='signup'),
path('login/', views.login, name='login'),
path('admin-signup/', views.adminsignup, name='admin-signup'),
path('events/', views.events, name='events'),
path('clubs/', views.clubs, name='clubs'),
path('workshops/', views.workshop, name='workshops'),
path('announcements/', views.announcements, name='announcements'),
path('events/<int:id>/', views.delete_event, name='delete-event'),
path('clubs/<int:id>/', views.delete_club, name='delete-club'),
path('workshops/<int:id>/', views.delete_workshop, name='delete-workshop'),
path('announcements/<int:id>/', views.delete_announcement, name='delete-announcement'),
path('events/<int:event_id>/register/', views.register_event, name='register-event'),
path('clubs/<int:club_id>/join/', views.join_club, name='join-club'),
path('workshops/<int:workshop_id>/register/', views.register_workshop, name='register-workshop'),
path('my-events/', views.my_events, name='my-events'),
path('my-clubs/', views.my_clubs, name='my-clubs'),
path('my-workshops/', views.my_workshops, name='my-workshops'),
path('events/<int:event_id>/registrations/', views.event_registrations, name='event-registrations'),
path('clubs/<int:club_id>/memberships/', views.club_memberships, name='club-memberships'),
path('workshops/<int:workshop_id>/registrations/', views.workshop_registrations, name='workshop-registrations'),
path('stats/', views.stats, name='stats'),
]

