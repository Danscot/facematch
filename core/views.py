from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Image
from django.views.decorators.http import require_GET
import random


# Create your views here.


def main(request):

    return render(request, 'index.html')


def top_images(request):
    # Get top 10 images sorted by votes descending and name ascending
    top_images = Image.objects.order_by('-votes', 'name')[:10]
    context = {
        'top_images': top_images
    }
    return render(request, 'rank.html', context)

# image_voting/views.py
@require_GET
def get_images(request):
    images = list(Image.objects.all())
    left_image = random.choice(images)
    right_image = random.choice(images)
    while left_image == right_image:
        right_image = random.choice(images)

    data = {
        'left_image_name': left_image.name,
        'left_image_path': left_image.path,
        'right_image_name': right_image.name,
        'right_image_path': right_image.path
    }
    return JsonResponse(data)

@require_GET
def vote(request):
    chosen_image_name = request.GET.get('chosen')
    other_image_name = request.GET.get('other')

    chosen_image = get_object_or_404(Image, name=chosen_image_name)
    other_image = get_object_or_404(Image, name=other_image_name)

    chosen_image.votes += 1
    chosen_image.save()

    other_image.votes -= 1
    other_image.save()

    return JsonResponse({'status': 'success'})
