from django.shortcuts import render, redirect,  get_object_or_404
from .models import Comment 
from articles.models import Article
from . import forms
from .forms import CommentForm 

 
# Create your views here.


def post_comment(request):
	if request.method == 'POST':
	  form = forms.CommentForm(request.POST, request.FILES)
	  if form.is_valid():
	  	comment = form.save(commit=False)
	  	comment.save() 
	  	return redirect('comments:view_comment')
	  	
	  	
      
         
	else:	
	  form = forms.CommentForm()
	return render(request, 'comments/post_comment.html', {'form': form})	

    

def view_comment(request):
	comments = Comment.objects.all().order_by('created_on')
	return render(request,'comments/view_comment.html', {'comments':comments})
     