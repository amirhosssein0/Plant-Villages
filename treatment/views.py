from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import TreatmentUploadForm
from .models import TreatmentUpload
from config.celery import app
from .tasks import classify_plant_image
from celery.result import AsyncResult
from django.http import JsonResponse, HttpResponseRedirect
import logging
from django.views import View


logger = logging.getLogger(__name__)

class TreatmentView(FormView):
    template_name = 'treatment/treatment.html'
    form_class = TreatmentUploadForm
    success_url = reverse_lazy('treatment:treatment')

    def form_valid(self, form):
        try:
            upload = TreatmentUpload.objects.create(
                photo=form.cleaned_data['photo'],
                description=form.cleaned_data['description']
            )
            task = classify_plant_image.delay(upload.photo.path)
            upload.task_id = task.id
            upload.save()
            messages.success(self.request, 'Your plant photo was uploaded! Diagnosis is processing...')
            return HttpResponseRedirect(f"{reverse('treatment:treatment')}?task_id={task.id}")
        except Exception as e:
            logger.error(f"Error in form_valid: {str(e)}")
            messages.error(self.request, 'An error occurred while uploading your photo. Please try again.')
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_id = self.request.GET.get('task_id')
        if task_id:
            context['task_id'] = task_id
        return context

class TreatmentResultView(View):
    def get(self, request, task_id):
        try:
            result = AsyncResult(task_id)
            if result.ready():
                if isinstance(result.result, dict) and 'error' in result.result:
                    return JsonResponse({
                        'status': 'error',
                        'message': result.result['error']
                    })
                return JsonResponse({
                    'status': 'done',
                    'result': result.result
                })
            return JsonResponse({'status': 'processing'})
        except Exception as e:
            logger.error(f"Error in TreatmentResultView: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': 'An error occurred while fetching the diagnosis result. Please try again later.'
            })