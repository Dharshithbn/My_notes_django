from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.contrib import messages

# Create your views here.


def index(request):

    notes = Note.objects.all().order_by('date').reverse()
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            note_txt = form.cleaned_data['note']
            db_note = Note(note_text=note_txt)
            db_note.save()
            messages.success(request,'Task saved successfully')
            return redirect('index') 
            # use "/" for redirect when the ul is empty like ''

    else:
        form = NoteForm()


    context ={
        'notes': notes,
        'form' : form
    }
    return render(request,"notes/index.html", context )

def delete(request,id):

    note = Note.objects.get(pk = id)
    note.delete()

    return redirect('index') 
     