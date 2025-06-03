from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def classify_plant_image(image_path):
    try:
        from transformers import pipeline
        from PIL import Image
        import os

        # Check if file exists
        if not os.path.exists(image_path):
            logger.error(f"Image file not found: {image_path}")
            return {'error': 'Image file not found'}

        # Check if model directory exists
        model_path = os.path.join('treatment', 'model', 'plantvillage-model')
        if not os.path.exists(model_path):
            logger.error(f"Model directory not found: {model_path}")
            return {'error': 'Model not found'}

        classifier = pipeline("image-classification", model=model_path)
        image = Image.open(image_path)
        results = classifier(image)
        return results
    except Exception as e:
        logger.error(f"Error in classify_plant_image: {str(e)}")
        return {'error': str(e)}