from django.shortcuts import render
from .utils import recommend_crop
from django.http import JsonResponse
import logging

# Set up logging
logger = logging.getLogger(__name__)

def home_view(request):
    return render(request, 'home.html')

def recommend(request):
    if request.method == "POST":
        try:
            # Extract features from POST data
            N = float(request.POST.get('nitrogen'))
            P= float(request.POST.get('phosphorus'))
            K = float(request.POST.get('potassium'))
            temperature = float(request.POST.get('temperature'))
            humidity = float(request.POST.get('humidity'))
            ph = float(request.POST.get('ph'))
            rainfall = float(request.POST.get('rainfall'))

            # Prepare the features list
            features = [N, P, K, temperature, humidity, ph, rainfall]
      
      
            # Log the input features to ensure they're correct
            logger.info(f"Input Features: {features}")

            # Predict crop recommendation
            recommended_crop = recommend_crop(features)

            # Return result as JSON
            return JsonResponse({'result': recommended_crop})

        except Exception as e:
            logger.error(f"Error in recommendation: {str(e)}")
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, "index.html")

  # Render a homepage template


# def recommend(request):
#     if request.method == "POST":
#         try:
#             # Extract features from POST data
#             nitrogen = float(request.POST.get('nitrogen'))
#             phosphorus = float(request.POST.get('phosphorus'))
#             potassium = float(request.POST.get('potassium'))
#             temperature = float(request.POST.get('temperature'))
#             humidity = float(request.POST.get('humidity'))
#             ph = float(request.POST.get('ph'))
#             rainfall = float(request.POST.get('rainfall'))

#             # Predict crop recommendation
#             features = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
#             recommended_crop = recommend_crop(features)

#             # Return result as JSON
#             return JsonResponse({'result': recommended_crop})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return render(request, "index.html")


