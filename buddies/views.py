from .forms import BuddyForm, NewBuddyForm
from django.shortcuts import render, redirect
from email.message import EmailMessage
from .models import Person

# relative import of forms
from .forms import BuddyForm

# Create your views here.


def index(request):
  return
  


  


# Saves submitted information into form
def create(request):
  if request.method == "POST":
    new_buddy = NewBuddyForm(request.POST)
    new_buddy.save()

    first_names = []
    last_names = []
    emails = []
    #Save four input variables
    major = request.POST.get('Major')
    Course_Number = request.POST.get('CourseNumber')

    #Find group member information 
    
    accounts = Person.objects.filter(Major__icontains = major, CourseNumber__icontains = Course_Number, has_group1 = False)[:3]
    if len(accounts) == 3:

      for account in accounts:
        first_names.append(account.first_name)
        last_names.append(account.last_name)
        emails.append(account.contact_email)
      
      #Send email to all three group members 
      email(first_names, last_names, emails, major, Course_Number)

      #Set hasgroup boolean to true
      for account in accounts:
        account.has_group1 = True
        account.save()
  return redirect("/services.html")

def email(first_names, last_names, emails, major, Course_Number):
  import smtplib
  gmail_user = "psetbuddy2021@gmail.com" # (You should provide your gmail account name)
  gmail_pwd = "testbuddy2021" # (You should provide your gmail password)
  smtpserver = smtplib.SMTP("smtp.gmail.com",587)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo
  smtpserver.login(gmail_user, gmail_pwd)
  subject = "PSETBuddy - Your Study Group Has Been Found!"
  to = emails
  msg = "Welcome to PSETBuddy! \n\n Your group members for " + major + Course_Number + " are: \n\n" + " - "+ first_names[0] + " " + last_names[0] + " (" + emails[0] + ")\n" + " - "+ first_names[1] + " " + last_names[1] + " (" + emails[1] + ")\n" + " - "+ first_names[2] + " " + last_names[2] + " (" + emails[2] + ")\n" + "\nBest of luck studying and be sure to always abide by the Honor Code!\n\n" + " Best, \n\n" + " The PSETBuddy Team"
  
  body = 'Subject: {}\n\n{}'.format(subject, msg)
  smtpserver.sendmail(gmail_user, to, body)
  smtpserver.close()
    
    

def addbuddy(request):
  context = {}
  context["new_buddy_form"] = NewBuddyForm()
  return render(request, "services.html", context)



