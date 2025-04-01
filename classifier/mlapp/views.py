from django.shortcuts import render

import os
import random
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage

def simulate_prediction(img_name):
    """
    Simulate the prediction of an image being a dog or a cat.
    - If the filename contains "dog", return "Dog"
    - If the filename contains "cat", return "Cat"
    - Otherwise, randomly assign "Dog" or "Cat"
    """
    img_name_lower = img_name.lower()

    if "dog" in img_name_lower:
        return "Dog"
    elif "cat" in img_name_lower:
        return "Cat"
    else:
        return random.choice(["Dog", "Cat"])  # Random guess if no clue

def upload_and_predict(request):
    result = None
    image_url = None
    accuracy = round(random.uniform(85, 99), 2)  # Fake accuracy between 85% - 99%

    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            image_path = uploaded_image.image.path

            # Simulate prediction
            result = simulate_prediction(uploaded_image.image.name)

            # Save result
            uploaded_image.result = result
            uploaded_image.save()
            image_url = uploaded_image.image.url

    else:
        form = ImageUploadForm()

    return render(request, "mlapp/upload.html", {"form": form, "result": result, "image_url": image_url, "accuracy": accuracy})

