from django.shortcuts import render
from coloring.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_author_by_name(authorname): 
  author = None
  
  # check if an Author with name 'authorname' already exists
  if Author.objects.filter(name = authorname).exists():
    # if so, fetch that object from the database
    author = Author.objects.get(name=authorname)
    
  else: 
    # otherwise, create a new Author with the name authorname
    author = Author(name = authorname)
    # save the created object
    author.save()

  return author



@csrf_exempt
def index(request, authorname="DefaultAuthor", dtitle=None):

  print("The authorname is:", authorname)
  print("dtitle:", dtitle);
  author = get_author_by_name(authorname)
  
  if request.POST: 
    # POST request received
    
    # demonstrating printing out the POST request & data
    print("Received POST request with data:")
    data = json.loads(request.body.decode('UTF-8'))
    print(data)

    # find out if a Drawing with the Author and Title already exists?
    # if it doesn't exist, you may create a new Drawing object
    # if it does exist, you may update an existing Drawing object

    if dtitle == None:
      dtitle = data['title']
    
    drawing = None
    if DrawingModel.objects.filter(title=dtitle, author=authorname).exists():
      drawing = DrawingModel.objects.get(title=dtitle, author=authorname)
    else:
      drawing = DrawingModel(title=dtitle, author=authorname)

    print("Title: "+ dtitle);
    
    drawing.points = data['points']
    drawing.save()

    author.lastDrawing = dtitle
    author.save()
    
    # make sure to save your object after creating or updating 
    # for more information, see get_author_by_name() and reference below
    # https://docs.djangoproject.com/en/4.0/ref/models/instances/#saving-objects
    
    return HttpResponse(True)

  else: 
    # GET request received

    # if a drawing by the author already exists,
    # send the drawing conent and title with the data below

    if dtitle == None:
      dtitle = author.lastDrawing
    
    drawing = None
    if dtitle != None:
      drawing = DrawingModel.objects.get(title=dtitle, author=authorname);
    
    data = {
      "author": author,
      "drawing": drawing
    }
    
    return render(request, 'coloring/index.html', data)