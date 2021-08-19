from rest_framework import viewsets
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from saveTextApp.models import Tag
from saveTextApp.serializer.serializers import TagSerializer



class TagCrud(viewsets.ViewSet):
	def list(self, request):
		"""Getting all item in tag table"""
		try:
			tags = Tag.objects.all()
			serializer = TagSerializer(tags, many=True)
			return Response({"count": tags.count(), 'results': serializer.data}, status=status.HTTP_200_OK)
		except: 
			raise Http404

	def retrieve(self, request, pk=None):
		"""For gettting single tag"""
		try:
			tag = Tag.objects.get(pk=pk )
			serializer = TagSerializer(tag)
			return Response({'results': serializer.data}, status=status.HTTP_200_OK)
		except: 
			raise Http404
