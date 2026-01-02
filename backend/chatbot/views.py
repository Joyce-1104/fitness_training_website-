from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "").lower()

        response = "Sorry, I didn’t understand that. Please ask about programs, timings, or membership."

        if any(word in message for word in ["hi", "hello", "hey"]):
            response = "Hello! Welcome to our Fitness Center. How can I help you today?"

        elif "program" in message:
            response = (
                "We offer Weight Loss, Strength Training, Yoga, Zumba, and Cardio programs."
            )

        elif "timing" in message or "open" in message:
            response = "Our gym is open Monday to Sunday, from 5 AM to 10 PM."

        elif "membership" in message or "price" in message:
            response = "Membership details are available on our Membership page."

        elif "trainer" in message:
            response = "Our certified trainers guide you with personalized workout plans."

        elif "contact" in message:
            response = "You can reach us through the Contact page or visit the gym directly."

        return JsonResponse({"reply": response})

    return JsonResponse({"error": "Invalid request"}, status=400)
