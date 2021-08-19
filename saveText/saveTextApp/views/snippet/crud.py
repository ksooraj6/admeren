from rest_framework import viewsets
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from saveTextApp.models import Tag, Savetext
from saveTextApp.serializer.serializers import TextSerializer



class SnippetCrud(viewsets.ViewSet):
	def list(self, request):
		"""Sending all data stored by the user """
		try:
			texts = Savetext.objects.filter(user= request.user.id)
			serializer = TextSerializer(texts, many=True)

			return Response({"count": texts.count(), 'results': serializer.data}, status=status.HTTP_200_OK)
		except: 
			raise Http404


	def create(self, request):
		"""For creating new text"""
		try:
			request.data.update({"user": request.user.id})
			serializer = TextSerializer(data= request.data)
			tag, create = Tag.objects.get_or_create(tag_title = request.data["title"])
			print(tag.id)
			request.data.update({"tag": tag.id})

			print(request.data)
			if serializer.is_valid(raise_exception=True):
				text = serializer.save()
				return Response({"count": "Success"}, status=status.HTTP_201_CREATED)
			return Response({"success": 1})
		except:
			raise Http404

	def retrieve(self, request, pk=None):
		"""For gettting single text"""
		try:
			text = Savetext.objects.get(pk=pk )
			serializer = TextSerializer(text)
			return Response({'results': serializer.data}, status=status.HTTP_200_OK)
		except: 
			raise Http404

	def update(self, request, pk=None):
		"""Upating the title"""
		try:
			instance = Savetext.objects.get(pk=pk)
			serializer = TextSerializer(instance, data=request.data)
			if serializer.is_valid(raise_exception=True):
				text = serializer.save()
				return Response({'title': text.title}, status=status.HTTP_200_OK)
			return Response({'error': "Something went wrong is serializer"}, status=status.HTTP_200_OK)
		except:
			raise Http404

	def destroy(self, request, pk=None):
		"""deleting title"""
		try:
			instance = Savetext.objects.get(pk=pk)
			instance.delete()
			return Response({'Success': 1}, status=status.HTTP_204_NO_CONTENT)
		except:
			raise Http404
