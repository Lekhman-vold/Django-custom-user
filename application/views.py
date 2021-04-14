from django.shortcuts import render
from django.views.generic import FormView

from .forms import SignUpForm


class UserForm(FormView):
    form_class = SignUpForm
    template_name = 'form_user.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def user_form(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=True)
#             new_user.save()
#         else:
#             SignUpForm()
#     return render(request, 'base.html', {'user_form': user_form})
