# writing_assignment/tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment
from .forms import AssignmentForm

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'tasks/assignment_list.html', {'assignments': assignments})

def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    return render(request, 'tasks/assignment_detail.html', {'assignment': assignment})

def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'tasks/create_assignment.html', {'form': form})

def update_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'tasks/update_assignment.html', {'form': form, 'assignment': assignment})

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')
    return render(request, 'tasks/delete_assignment.html', {'assignment': assignment})
