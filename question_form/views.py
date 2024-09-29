from django.shortcuts import render, HttpResponse
from .forms import QuestionForm

def question_create(request):
     if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form-success.html')
        else:
            return HttpResponse("invalid")
     form = {'form':QuestionForm}
     return render(request,'questin_form.html',form)

        
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_form/question_list.html/', questions)
