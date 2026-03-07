from django.shortcuts import render
from django.http import JsonResponse
import json

def chat(request):

    if request.method == "POST":
        
        try:
            data = json.loads(request.body)

            user_message = data.get("message")

            response = {
                "message_received": user_message,
                "reply": "Chatbot backend is working!"
            }

            return JsonResponse(response)

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Only POST request allowed"})