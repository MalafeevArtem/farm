from django.contrib import messages
from django.shortcuts import get_object_or_404 , redirect , render
from django.views import View
from django.views.generic import DetailView , ListView

from fields.forms import FieldForm
from fields.models import Crop, Field


class FieldsView(ListView):
    """Список полей"""
    model = Field
    context_object_name = 'fields'
    template_name = 'fields/field_list.html'


class FieldDetail(DetailView):
    """Детальная информация о поле"""
    model = Field
    context_object_name = 'field'
    template_name = 'fields/field_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crops_list'] = self.object.crops.all()  # Добавляем информацию по севам

        return context


class FieldCreateView(View):
    """Создание нового поля"""
    def get(self, request):
        return render(request, 'fields/field_add.html', {'form': FieldForm()})

    def post(self, request):
        user = request.user
        form = FieldForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            field = form.save(commit=False)
            field.user = user
            field.save()

            return redirect('/fields/')

        messages.add_message(request, messages.INFO, 'Поле с таким именем уже существует!')

        return render(request, 'fields/field_add.html', {'form': FieldForm()})


class FieldEditView(View):
    """Редактирование поля"""
    def get(self, request, slug):
        instance = get_object_or_404(Field, slug=slug)

        return render(request, 'fields/field_add.html',
                      {'form': FieldForm(instance=instance)})

    def post(self, request, slug):
        instance = get_object_or_404(Field, slug=slug)
        form = FieldForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()

            return redirect('/fields/{}/'.format(slug))

        messages.add_message(request, messages.INFO, 'Данные неккоректны')

        return render(request, 'fields/field_add.html', {'form': FieldForm()})



# class CropView(View):
#     def get(self, request):
#         crops = Field.objects.prefetch_related().all()
#
#         for crop in crops:
#             print('{}'.format(crop.name, crop.season))
#
#         return render(request, 'fields/field_add.html', {'form': FieldForm()})