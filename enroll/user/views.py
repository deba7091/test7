from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.models import *
 
from user.serializers import Userserializer
from user.serializers import Skillserializer
from django.db import transaction
from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render
#from enroll.settings import ITEMS_PER_PAGE
#import mysql.connector


class UserView(APIView):
   def get_object(self,id):
        try:
            return User.objects.get(id = id)
        except User.DoesNotExist:
            raise Http404
   def post(self,request):
        try:
            with transaction.atomic():
                user_serializer=Userserializer(data=request.data)
                if user_serializer.is_valid():
                    user_serializer=user_serializer.save()
                    return Response({'msg':'Created Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)                        
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        
   
   def get(self,request,id=None):
        if id:
             userData =User.objects.filter(id=id).select_related("user").values(
                'id','fullname','mobile','email','password','address').first()
             if userData is None:
                 return Response({'msg':'Not Found ! '}, status=status.HTTP_404_NOT_FOUND)
             return Response(userData,status=status.HTTP_200_OK)  
        else:
            user = User.objects.all()            
            serializer = Userserializer(user, many=True)
            userData=serializer.data
            if len(userData)>0:
                return Response(userData, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'Not Found ! '}, status=status.HTTP_404_NOT_FOUND)
            
   def put(self,request,id=None):
            try:
                with transaction.atomic():
                    userData = userData =User.objects.filter(id=id).first()
                    user_serializer=Userserializer(userData, data=request.data)
                    if user_serializer.is_valid():
                        user_serializer=user_serializer.save()
                        return Response({'msg':'updated Successfully'}, status=status.HTTP_200_OK)
                    else:
                        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)         
            except Exception as e:
                error = getattr(e, 'message', repr(e))
                return Response(error,status=status.HTTP_400_BAD_REQUEST)



class SkillView(APIView):
   def get_object(self,id):
        try:
            return Skill.objects.get(id = id)
        except Skill.DoesNotExist:
            raise Http404
   def post(self,request):
        try:
            with transaction.atomic():
                Skill_serializer=Skillserializer(data=request.data)
                if Skill_serializer.is_valid():
                    Skill_serializer=Skill_serializer.save()
                    return Response({'msg':'Created Successfully'}, status=status.HTTP_200_OK)
                else:
                    return Response(Skill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)                        
        except Exception as e:
            error = getattr(e, 'message', repr(e))
            return Response(error,status=status.HTTP_400_BAD_REQUEST)
        
   
   def get(self,request,id=None):
        if id:
             userData =Skill.objects.filter(id=id).select_related("Skill").values(
                'id','skills').first()
             if userData is None:
                 return Response({'msg':'Not Found ! '}, status=status.HTTP_404_NOT_FOUND)
             return Response(userData,status=status.HTTP_200_OK)  
        else:
            user = Skill.objects.all()            
            serializer = Skillserializer(user, many=True)
            userData=serializer.data
            if len(userData)>0:
                return Response(userData, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'Not Found ! '}, status=status.HTTP_404_NOT_FOUND)
            
   def put(self,request,id=None):
            try:
                with transaction.atomic():
                    userData = userData =Skill.objects.filter(id=id).first()
                    Skill_serializer=Skillserializer(userData, data=request.data)
                    if Skill_serializer.is_valid():
                        Skill_serializer=Skill_serializer.save()
                        return Response({'msg':'updated Successfully'}, status=status.HTTP_200_OK)
                    else:
                        return Response(Skill_serializer.errors, status=status.HTTP_400_BAD_REQUEST)         
            except Exception as e:
                error = getattr(e, 'message', repr(e))
                return Response(error,status=status.HTTP_400_BAD_REQUEST)


class Combinedata(APIView):
    def get(self, request,id):
        data = []
        response = {}
        user = User.objects.filter(id=id)
       # list1=[i.id for i in user ][0]
        #print(list1)

        if len(user)>0:
            for Record in user:
                response = {
                    "id":Record.id,
                    "user" : Record.id,
                    "mobile" : Record.mobile,
                    "email" : Record.email,
                    "password" : Record.password,
                    "address" : Record.address,
                    'skills':{i.skills for i in Record.skills.all() },
            
                }                
        data.append(response)
        return Response(data,status=status.HTTP_200_OK)

           
class listing(APIView):
    def get(self,request,page=None):
        data = []
        search = request.GET.get("search")
        limit = 3
        page = int(request.GET.get("page",1))
        size = limit
        start = (page - 1) * size
        end = start + size
        
        page=request.GET.get('page')
        print(page)
        if page !=None:
             user = User.objects.all()
             serializer = Userserializer(user, many=True)
             userData=serializer.data
             no_of_record=len(userData)
             userData=userData[int(start):int(end)]
             
             list1=[]
             for i in userData:
                 list1.append(i)
                 
             if len(list1)>0:
                list_data = {"total_records": no_of_record, "limit": limit, "offset": start, "data": list1}

                return Response(list_data,status=status.HTTP_200_OK)
                     
                      
                     
                                   
                  
                
        # else:
        #     user = User.objects.all()            
        #     serializer = Userserializer(user, many=True)
        #     userData=serializer.data
        #     if len(userData)>0:
        #         return Response(userData, status=status.HTTP_200_OK)
        #     else:
        #         return Response({'msg':'Not Found ! '}, status=status.HTTP_404_NOT_FOUND)