import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# View to render the calculator page
def calculator_view(request):
    return render(request, 'calculator/calculator.html')

# View to handle POST requests for calculations
@csrf_exempt  # Temporarily disable CSRF for testing, avoid in production
def calculate_view(request):
    if request.method == 'POST':
        try:
            # Get the expression from the request body
            data = json.loads(request.body)
            expression = data['expression']
            
            # Evaluate the expression (use with caution in production)
            result = eval(expression)
            
            # Return the result as JSON
            return JsonResponse({'result': result})
        except Exception as e:
            # Handle errors in the calculation (e.g., syntax errors)
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
