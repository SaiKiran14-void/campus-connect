from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import SignupSerializer, LoginSerializer, AdminSignupSerializer, EventSerializer, ClubSerializer, WorkshopSerializer, AnnouncementSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from api.models import UserProfile, Event, Club, Workshop, Announcement, Registration, ClubMembership, WorkshopRegistration
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data = request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            profile = UserProfile.objects.get(user=user)
            role = profile.role
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response({
                'access': access_token,
                'refresh': refresh_token,
                'role': role
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def adminsignup(request):
    serializer = AdminSignupSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def events(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)
        
    if request.method == 'POST':
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])  
def clubs(request):
    if request.method == 'GET':
        clubs = Club.objects.all()
        serializer = ClubSerializer(clubs, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ClubSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', "POST"])
def workshop(request):
    if request.method == 'GET':
        workshop = Workshop.objects.all()
        serializer = WorkshopSerializer(workshop, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = WorkshopSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', "POST"])
def announcements(request):
    if request.method == 'GET':
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AnnouncementSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['DELETE'])
def delete_event(request, id):
    try:
        event = Event.objects.get(id=id)
        event.delete()
        return Response({'message': 'Event deleted!'}, status=status.HTTP_204_NO_CONTENT)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found!'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_club(request, id):
    try:
        club = Club.objects.get(id=id)
        club.delete()
        return Response({'message': 'Club deleted!'}, status=status.HTTP_204_NO_CONTENT)
    except Club.DoesNotExist:
        return Response({'error': 'Club not found!'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_workshop(request, id):
    try:
        workshop = Workshop.objects.get(id=id)
        workshop.delete()
        return Response({'message': 'Workshop deleted!'}, status=status.HTTP_204_NO_CONTENT)
    except Workshop.DoesNotExist:
        return Response({'error': 'Workshop not found!'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_announcement(request, id):
    try:
        announcement = Announcement.objects.get(id=id)
        announcement.delete()
        return Response({'message': 'Announcement deleted!'}, status=status.HTTP_204_NO_CONTENT)
    except Announcement.DoesNotExist:
        return Response({'error': 'Announcement not found!'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        Registration.objects.create(student=request.user, event=event)
        return Response({'message': 'Registered successfully!'}, status=status.HTTP_201_CREATED)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found!'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Already registered!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_club(request, club_id):
    try:
        club = Club.objects.get(id=club_id)
        ClubMembership.objects.create(student=request.user, club=club)
        return Response({'message': 'Joined successfully!'}, status=status.HTTP_201_CREATED)
    except Club.DoesNotExist:
        return Response({'error': 'Club not found!'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Already a member!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_workshop(request, workshop_id):
    try:
        workshop = Workshop.objects.get(id=workshop_id)
        WorkshopRegistration.objects.create(student=request.user, workshop=workshop)
        return Response({'message': 'Registered successfully!'}, status=status.HTTP_201_CREATED)
    except Workshop.DoesNotExist:
        return Response({'error': 'Workshop not found!'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'error': 'Already registered!'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_events(request):
    registrations = Registration.objects.filter(student=request.user)
    events = [reg.event for reg in registrations]
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_clubs(request):
    memberships = ClubMembership.objects.filter(student=request.user)
    clubs = [mem.club for mem in memberships]
    serializer = ClubSerializer(clubs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_workshops(request):
    registrations = WorkshopRegistration.objects.filter(student=request.user)
    workshops = [reg.workshop for reg in registrations]
    serializer = WorkshopSerializer(workshops, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def event_registrations(request, event_id):
    count = Registration.objects.filter(event_id=event_id).count()
    students = Registration.objects.filter(event_id=event_id).values_list('student__username', flat=True)
    return Response({'count': count, 'students': list(students)})

@api_view(['GET'])
def club_memberships(request, club_id):
    count = ClubMembership.objects.filter(club_id=club_id).count()
    students = ClubMembership.objects.filter(club_id=club_id).values_list('student__username', flat=True)
    return Response({'count': count, 'students': list(students)})

@api_view(['GET'])
def workshop_registrations(request, workshop_id):
    count = WorkshopRegistration.objects.filter(workshop_id=workshop_id).count()
    students = WorkshopRegistration.objects.filter(workshop_id=workshop_id).values_list('student__username', flat=True)
    return Response({'count': count, 'students': list(students)})

@api_view(['GET'])
def stats(request):
    from django.contrib.auth.models import User
    total_students = UserProfile.objects.filter(role='student').count()
    total_admins = UserProfile.objects.filter(role='admin').count()
    total_events = Event.objects.count()
    total_clubs = Club.objects.count()
    total_workshops = Workshop.objects.count()
    total_announcements = Announcement.objects.count()
    return Response({
        'students': total_students,
        'admins': total_admins,
        'events': total_events,
        'clubs': total_clubs,
        'workshops': total_workshops,
        'announcements': total_announcements,
    })