from django.urls import path
from .views import chatbot_home, chat, get_chat_history

urlpatterns = [
    path("", chatbot_home, name="chatbot_home"),
    path("chat/", chat, name="chat_api"),
    path("history/", get_chat_history, name="chat_history"),
]