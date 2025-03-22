from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from students.models import Student
from employees.models import Employee
from rest_framework import serializers
from .serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins,viewsets
from blogs.models import Blog,Comment
from .serializers import BlogSerializer,CommentSerializer
from .paginations import CustomPagination
from . filters import employeeFilter
from rest_framework.filters import SearchFilter,OrderingFilter

#Function Based Views

@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':       
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        student  = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    

# #Class Based Views
       
# class employeesView(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# class employeeDetailView(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
    
#     def get(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee,data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Views using mixins


# class employeesView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class employeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView) :
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self,request,pk) :
#         return self.retrieve(request,pk)
    
#     def put(self,request,pk) :
#         return self.update(request,pk)
    
#     def delete(self,request,pk) :
#         return self.destroy(request,pk)
    

# # Generics View

# class employeesView(generics.ListCreateAPIView) :
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
# class employeeDetailView(generics.RetrieveUpdateDestroyAPIView) :
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'


#Model viewsets view

class EmployeeViewSet(viewsets.ModelViewSet) :
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = employeeFilter
    
    
# Views for blogs

class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_title','blog_content']
    ordering_fields = ['id']
    
    
    

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'    



class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'              