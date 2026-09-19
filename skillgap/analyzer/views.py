from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# ✅ Home page
def index(request):
    return render(request, "index.html")


# ✅ AI response function
@csrf_exempt
def ai_response(request):
    if request.method != "POST":
        return JsonResponse({"reply": "Invalid request"})

    try:
        data = json.loads(request.body)
        user_input = data.get("message", "").lower().strip()
        print(f"📝 User: {user_input}")

        # 🔥 Responses dictionary (expanded)
        responses = {

            # Greeting
            "hi": "Hello! How are you doing today 😄",
            "hello": "Hi there! Ready to improve your skills?",
            "bye": "See you later! Keep learning 🚀",
            "thank you": "You're welcome! 💪",

            # General AI
            "what is ai": "AI (Artificial Intelligence) allows machines to think and learn like humans.",
            "what is machine learning": "Machine Learning is a subset of AI where systems learn from data.",
            "what is deep learning": "Deep Learning uses neural networks for complex tasks.",
            "what is nlp": "NLP helps computers understand human language.",
            "what is chatbot": "A chatbot is a program that communicates with users.",
            "types of chatbot": "There are rule-based and AI-based chatbots.",
            "is this ai": "This is a rule-based chatbot, not full AI.",
            "what is prompt": "Prompt is input given to AI.",
            "what is generative ai": "Generative AI creates content like text, images, etc.",

            # 🔥 AI TOOLS (IMPORTANT)
            "ai tools": "Popular AI tools are: ChatGPT, Gemini, GitHub Copilot, Grammarly, Canva AI, Notion AI, Midjourney, DALL-E, Runway ML, Perplexity AI.",
            "what are ai tools": "AI tools help automate tasks. Examples: ChatGPT, Gemini, Copilot, Canva AI.",
            "chatgpt": "ChatGPT is an AI chatbot used for answering questions and coding help.",
            "gemini": "Gemini is Google's AI chatbot.",
            "copilot": "GitHub Copilot helps developers write code using AI.",
            "midjourney": "Midjourney generates AI images.",
            "dalle": "DALL-E creates images from text.",
            "grammarly": "Grammarly improves writing using AI.",
            "canva": "Canva provides AI-based design tools.",
            "notion ai": "Notion AI helps in writing and productivity.",
            "runway": "Runway ML is used for AI video editing.",
            "perplexity": "Perplexity AI is an AI search engine.",

            # Django / Code
            "what is django": "Django is a Python framework used to build web apps.",
            "what is view": "View handles request and returns response.",
            "what is json": "JSON is a data format used to send data.",
            "what is api": "API connects frontend and backend.",
            "what is rest api": "REST API uses HTTP methods like GET and POST.",
            "what is csrf": "CSRF prevents unauthorized requests.",
            "why post": "POST is used to send data securely.",
            "what is function": "Function is reusable block of code.",
            "what is loop": "Loop repeats code multiple times.",
            "what is exception": "Exception handles errors in code.",

            # Project
            "project": "This is a Skill Gap Analyzer chatbot.",
            "what problem": "It solves mismatch between skills and job requirements.",
            "features": "Resume analysis, skill match, missing skills, roadmap.",
            "skill gap": "Skill gap is difference between required and actual skills.",
            "resume": "Resume shows your skills and experience.",
            "job": "Focus on roles like Data Analyst or Full Stack Developer.",
            "future scope": "We can integrate real AI models for better accuracy.",
            "technologies": "Python, Django, HTML, CSS, JavaScript.",

            # Learning
            "learn python": "Start with basics, then build projects.",
            "learn sql": "Practice queries, joins, and subqueries.",
            "improve skills": "Practice daily and build real projects.",
            "interview": "Be confident and explain clearly.",
            "communication": "Improve speaking and clarity.",
            "coding": "Practice on platforms like LeetCode.",
            "motivation": "Stay consistent and never give up 💪",

            # Default
            "default": "Ask me about AI, AI tools, coding, resume, or jobs 😄"
        }

        # 🔥 Matching logic (improved)
        reply = responses["default"]

        for key, value in responses.items():
            if key != "default" and key in user_input:
                reply = value
                break

        print(f"🤖 Bot: {reply}")
        return JsonResponse({"reply": reply})

    except Exception as e:
        print(f"Error: {str(e)}")
        return JsonResponse({"reply": "Something went wrong 😢"})