from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets, filters, status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import User, Document, Profile, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal
from .serializers import DonationGoalsSerializers, VolunteerGoalsSerializers, DonationRecordSerializers, VolunteerRecordSerializers, DonationGoalBreakdownSerializer, ProfileSerializer, DocumentSerializer
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
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

class DonationGoalBreakdownView(generics.ListCreateAPIView):
    queryset = Donationgoal.objects.all()
    serializer_class = DonationGoalBreakdownSerializer
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

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