from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ChatMessage
from .chatbot_logic import get_chatbot_response

def chatbot_home(request):
    """Render the main chatbot page"""
    return render(request, 'chatbot/index.html')

def get_chat_history(request):
    """Get chat history for the user"""
    messages = ChatMessage.objects.all().order_by('created_at')[:50]
    data = [
        {
            'role': msg.role,
            'message': msg.message,
            'created_at': msg.created_at.isoformat()
        }
        for msg in messages
    ]
    return JsonResponse({'messages': data})

@csrf_exempt
def chat(request):
    """Handle chat API requests"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip()
            
            if not user_message:
                return JsonResponse({"error": "Message cannot be empty"})
            
            # Save user message
            user_msg = ChatMessage.objects.create(
                role='user',
                message=user_message
            )
            
            # Get chatbot response
            bot_response = get_chatbot_response(user_message)
            
            # Save bot response
            bot_msg = ChatMessage.objects.create(
                role='bot',
                message=bot_response
            )
            
            return JsonResponse({
                "success": True,
                "user_message": user_message,
                "bot_response": bot_response
            })
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Only POST request allowed"}, status=405)