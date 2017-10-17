import django_filters
from django.shortcuts import render
from rest_framework import viewsets

from service.models import Document, Corpus
from service.serializers import DocumentSerializer, CorpusSerializer


def homepage(request):
    return render(request, 'index.html')


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('status', 'quality', 'corpus')


class CorpusViewSet(viewsets.ModelViewSet):
    queryset = Corpus.objects.all()
    serializer_class = CorpusSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
