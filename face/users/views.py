from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
import face_recognition
import numpy as np
import base64
from rest_framework.views import APIView
import cv2 

from django.conf import settings
import os
import uuid
import io

from .models import User
import asyncio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.conf import settings
import os
import io
import base64
import uuid
from PIL import Image
# Create your views here.
class Checkuserexist(APIView):
    
    #serializer_class = UserSerializer
    def post(self,request):
        try:
            # Receive base64-encoded image from frontend
            image_data = request.data.get('image_data')

            if not image_data:
                return Response({'error': 'No image data provided'}, status=status.HTTP_400_BAD_REQUEST)
           
            img_data = base64.b64decode(image_data)
            #print("Decoded image data:", img_data)  # Debugging

            if not img_data:
                return Response({'error': 'Failed to decode image data'}, status=status.HTTP_400_BAD_REQUEST)

            # Convert to PIL Image
            image = Image.open(io.BytesIO(img_data))

            # Convert to numpy array
            image_np = np.array(image)
            face_locations = face_recognition.face_locations(image_np)
            #print("face locations",face_locations)
            if not face_locations:
                raise ValueError("No face detected in the provided image")
            
            # Use face_recognition library to get face encodings
            face_encodings = face_recognition.face_encodings(image_np, face_locations)
            #print("Face encodings:", face_encodings)
            
            if not face_encodings:
                raise Response({'error':'No face detected in the provided image'},status=status.HTTP_400_BAD_REQUEST)
            
            #face_encodings = face_recognition.face_encodings(img_np, face_locations)
            

            MATCH_THRESHOLD = 0.41

            #Compare with stored encodings
            for face_encoding in face_encodings:
                
                users = User.objects.all()
                #print("user",users)
                for user in users:
                    
                    stored_encoding = np.frombuffer(user.image_encoding, dtype=np.float64)
                    #print("stored encoding",stored_encoding)
                    match = face_recognition.compare_faces([stored_encoding], face_encoding)
                    print("match",match)
                    if match[0]:
                        return Response({'message':'User Found','user_id': user.id,'image_data': image_data}, status=status.HTTP_200_OK)
                    
                    # stored_encoding = np.frombuffer(user.image_encoding, dtype=np.float64)
                    # # Calculate the Euclidean distance between the encodings
                    # dist = distance.euclidean(stored_encoding, face_encoding)
                    # print("distance",dist)
                    # # Check if the distance is below the threshold
                    # if dist < MATCH_THRESHOLD:
                    #     print("match found",user.id,"distance",dist)
                    #     return Response({'message':'User Found','user_id': user.id,'image_data': image_data}, status=status.HTTP_200_OK)
                        
            # If no match found, store the new user
            user = User.objects.create(image_encoding=face_encodings[0].tobytes())
            return Response({'message':'User Created','user_id': user.id ,'image_data': image_data}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        