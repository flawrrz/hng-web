from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    person = {
        "slackUsername":"flawrrz", 
        "backend":True, 
        "age":16, 
        "bio":"Eager to learn",
    
    }
    return Response(person)
