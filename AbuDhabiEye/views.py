import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Database Actions
from AbuDhabiEye.db.actions.getUserDetails import getUserDetailsfromDB
from AbuDhabiEye.db.actions.updateUserDetails import updateUserDetails
from AbuDhabiEye.db.actions.getEvents import getAllCulturalEvents
from AbuDhabiEye.db.actions.getGroups import getAllTravelGroups

# AI Services
from AbuDhabiEye.Services.llm_service import LLM
from AbuDhabiEye.Services.prediction import prediction

# Langchain Utils
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

@csrf_exempt
def getUserDetails(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8")) 
        email = data.get("email")
        username = data.get("username")
        print(username, email)
        response = getUserDetailsfromDB(username, email)
        
        return JsonResponse({"user": response})
     
@csrf_exempt
def UpdateProfile(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8")) 
        details = data.get("user_details")
        response = updateUserDetails(details)
        
        if response:
            updated_user_details = getUserDetailsfromDB(response.get("username"), response.get("email"))
            print(updated_user_details)
            
        return JsonResponse({"user": updated_user_details})
    
    return JsonResponse({"user": response})

@csrf_exempt
def getEvent(request):
    if request.method == "GET":
        allEvents = getAllCulturalEvents()
        
        return JsonResponse({"events": allEvents})

@csrf_exempt
def getGroup(request):
    if request.method == "GET":
        allGroups = getAllTravelGroups()
        
        return JsonResponse({"groups": allGroups})
    
@csrf_exempt
def Ask(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8")) 
        user_prompt = data.get("prompt")
        llm_instance = LLM(token_limit=3000, model="gpt-4o-mini")
        llm = llm_instance.get_llm()
        output_parser = StrOutputParser()
        template = """
            You are a Tourism Abu Dhabi Tourism Assisstant who help tourist visit abu dhabi.
            
            
            Question: {Query}
        """
        prompt = ChatPromptTemplate.from_template(template=template)
        
        chain = prompt | llm | output_parser
        print(prediction(user_prompt))
        response = chain.invoke({"Query": user_prompt})
        return JsonResponse({"response": response})