from rest_framework.response import Response
from rest_framework import status, generics, pagination, serializers
from datetime import datetime
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
#Class
from blog_api.models.author import Author
from blog_api.serializers.authorSerializers import AuthorSerializer

class AuthorView(generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = pagination.PageNumberPagination

    @swagger_auto_schema(
        operation_description="Get a paginated list of Blog objects",
        manual_parameters=[
            openapi.Parameter('page', in_=openapi.IN_QUERY, description='Page number', type=openapi.TYPE_INTEGER),
            openapi.Parameter('page_size', in_=openapi.IN_QUERY, description='Number of items per page', type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: serializers.ListSerializer(child=AuthorSerializer()),
            400: "Bad Request",
        },
    )

    def get(self, request, *args, **kwargs):
        page = request.query_params.get('page')
        page_size = request.query_params.get('page_size')
        self.pagination_class.page_size = page_size or self.pagination_class.page_size
        page_queryset = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(page_queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "author": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_note(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        author = self.get_note(pk=pk)
        if author == None:
            return Response({"status": "fail", "message": f"Author with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(author)
        return Response({"status": "success", "author": serializer.data})

    def put(self, request, pk):
        author = self.get_note(pk)
        if author == None:
            return Response({"status": "fail", "message": f"Author with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "author": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_note(pk)
        if author == None:
            return Response({"status": "fail", "message": f"Blog with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)