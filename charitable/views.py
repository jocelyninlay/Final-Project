from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets, filters, status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from .models import User, Profile, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal, Document
from .serializers import DonationGoalsSerializers, VolunteerGoalsSerializers, DonationRecordSerializers, VolunteerRecordSerializers, DonationGoalBreakdownSerializer, ProfileSerializer, VolunteerGoalBreakdownSerializer, DocumentSerializer
from django.db.models import Q
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from dj_rest_auth.registration.views import SocialLoginView

# class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = CALLBACK_URL_YOU_SET_ON_GOOGLE
#     client_class = OAuth2Client

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from rest_framework.parsers import FileUploadParser


class DonationGoalListView(generics.ListCreateAPIView):
    queryset = Donationgoal.objects.all()
    serializer_class = DonationGoalsSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class DonationGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donationgoal.objects.all()
    serializer_class = DonationGoalsSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class VolunteerGoalListView(generics.ListCreateAPIView):
    queryset = Volunteergoal.objects.all()
    serializer_class = VolunteerGoalsSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class VolunteerGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volunteergoal.objects.all()
    serializer_class = VolunteerGoalsSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class DonationRecordListView(generics.ListCreateAPIView):
    queryset = Donationrecord.objects.all()
    serializer_class = DonationRecordSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly 

class DonationRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donationrecord.objects.all()
    serializer_class = DonationRecordSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class VolunteerRecordListView(generics.ListCreateAPIView):
    queryset = Volunteerrecord.objects.all()
    serializer_class = VolunteerRecordSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly 

class VolunteerRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volunteerrecord.objects.all()
    serializer_class = VolunteerRecordSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class DonationGoalBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationGoalBreakdownSerializer
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Donationgoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VolunteerGoalBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VolunteerGoalBreakdownSerializer
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Volunteergoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnnualIncomeView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()    
    serializer_class = ProfileSerializer
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class DocumentCreateView(CreateAPIView):
    model = Document
    fields = ['upload', ]
    success_url = reverse_lazy('home')
    serializer_class = DocumentSerializer
    parser_classes = [FileUploadParser]

    # def create(self, request, *args, **kwargs):
    #     breakpoint()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     documents = Document.objects.all()
    #     context['documents'] = documents
    #     return context