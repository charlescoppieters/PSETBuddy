from .forms import BuddyForm, NewBuddyForm, NewFeedbackForm
from django.shortcuts import render, redirect
from email.message import EmailMessage
from .models import Person
from .models import Feedback
#from django.utils import timezone

# relative import of forms
from .forms import BuddyForm

# Create your views here.


def index(request):
  return
  

# Saves submitted information into form
def create(request):
  from datetime import datetime, timedelta

  if request.method == "POST":
    new_buddy = NewBuddyForm(request.POST)
    #Save current time into model
    #Save into database 
    new_buddy.save()

    
    
    # Create data arrays 
    first_names = []
    last_names = []
    emails = []
    zoom_preferences = []
    time_zones = []
    time_managements = []

    #Save four input variables
    firstname = request.POST.get('first_name')
    lastname = request.POST.get('last_name')
    email = request.POST.get('contact_email')
    major = request.POST.get('Major')
    Course_Number = request.POST.get('CourseNumber')
    
    
    #Find big group of 9 to be optimized into 3 groups of 3 people
    
    accounts = Person.objects.filter(Major__icontains = major, CourseNumber__icontains = Course_Number, has_group1 = False)[:9]
    #once 9 people have signed up for one class, optimize
    if len(accounts) == 9:
      
      for account in accounts:
        first_names.append(account.first_name)
        last_names.append(account.last_name)
        emails.append(account.contact_email)
        time_zones.append(account.time_zone)
        time_managements.append(account.time_management)
        zoom_preferences.append(account.zoom_preference)

      groups = KNN(time_managements, time_zones, zoom_preferences)
      
      group1firstnames = []
      group1lastnames = []
      group1emails = []

      group2firstnames = []
      group2lastnames = []
      group2emails = []

      group3firstnames = []
      group3lastnames = []
      group3emails = []

      #Send emails to groups
      for i in range (3):
        group1firstnames.append(accounts[int(groups[0,i])].first_name)
        group1lastnames.append(accounts[int(groups[0,i])].last_name)
        group1emails.append(accounts[int(groups[0,i])].contact_email)
      
        group2firstnames.append(accounts[int(groups[1,i])].first_name)
        group2lastnames.append(accounts[int(groups[1,i])].last_name)
        group2emails.append(accounts[int(groups[1,i])].contact_email)
      
        group3firstnames.append(accounts[int(groups[2,i])].first_name)
        group3lastnames.append(accounts[int(groups[2,i])].last_name)
        group3emails.append(accounts[int(groups[2,i])].contact_email)


      emailFunc(group1firstnames, group1lastnames, group1emails, major, Course_Number)
      emailFunc(group2firstnames, group2lastnames, group2emails, major, Course_Number)
      emailFunc(group3firstnames, group3lastnames, group3emails, major, Course_Number)


      #Set hasgroup boolean to true
      for account in accounts:
        account.has_group1 = True
        account.save()
      
    #Check for people who have not been assinged to groups and send them dissapointment email
    # lone_wolves = Person.objects.filter(has_group1 = False)
      
    # for wolve in lone_wolves:
    #   if timezone.now() - timedelta(days = 21) > wolve.date:
    #     dissapointment_email(wolve.first_name, wolve.contact_email)
    #     wolve.has_group1 = True 
    #     wolve.save()


  return redirect("/services.html")

def KNN(time_managements, time_zones, zoom_preferences):
  import numpy as np
  import random as rd
  from sklearn.neighbors import KDTree
  points = np.array([[time_managements[0], time_zones[0], zoom_preferences[0]],
            [time_managements[1], time_zones[1], zoom_preferences[1]], 
            [time_managements[2], time_zones[2], zoom_preferences[2]], 
            [time_managements[3], time_zones[3], zoom_preferences[3]], 
            [time_managements[4], time_zones[4], zoom_preferences[4]], 
            [time_managements[5], time_zones[5], zoom_preferences[5]], 
            [time_managements[6], time_zones[6], zoom_preferences[6]], 
            [time_managements[7], time_zones[7], zoom_preferences[7]], 
            [time_managements[8], time_zones[8], zoom_preferences[8]]])
  tree = KDTree(points)
  nearest_dist, nearest_ind = tree.query(points, k=3)  # k=3 nearest neighbors where k1 = identity, so 2 nearest neighbors others than identity
  
  #Make groups 
  from numpy import random 
  randomValue1 = random.randint(8)
  allPeople = np.array([0,1,2,3,4,5,6,7,8])
  groupA = np.array(nearest_ind[0, :])
  memberA1 = nearest_ind[0, 0]
  memberA2 = nearest_ind[0,1]
  memberA3 = nearest_ind[0,2]
  groupB = np.zeros(3)
  bChecker = 0
  #Find group B 
  for i in range (9):
    if memberA1 not in nearest_ind[i, :] or memberA2 not in nearest_ind[i, :] or memberA3 not in nearest_ind[i, :] :
      groupB = nearest_ind[i, :]
      bChecker += 1
  if bChecker == 0:
    groupBList = []
    breakCounter = 0
    for k in range (9):
      if allPeople[k] not in groupA & breakCounter < 3:
        groupBList.append(k)
        breakCounter += 1
    groupB = np.array(groupBList)
           
  #Formulate group C 
  
  groupCList = []
  for i in range (9):
    if allPeople[i] not in groupA and allPeople[i] not in groupB:
      groupCList.append(i)
  groupC = np.array(groupCList)
  groups = np.array([groupA, groupB, groupC])
  return groups
  
    

def emailFunc(first_names, last_names, emails, major, Course_Number):
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
  msg = "Welcome to PSETBuddy! \n\n Your group members for " + major + Course_Number + " are: \n\n" + " - "+ first_names[0] + " " + last_names[0] + " (" + emails[0] + ")\n" + " - "+ first_names[1] + " " + last_names[1] + " (" + emails[1] + ")\n" + " - "+ first_names[2] + " " + last_names[2] + " (" + emails[2] + ")\n" + "\nBest of luck studying and be sure to always abide by the Honor Code!\n\n" + "Best, \n\n" + "The PSETBuddy Team"
  body = "Subject: {}\n\n{}".format(subject, msg)
  smtpserver.sendmail(gmail_user, to, body)
  smtpserver.close()

def dissapointment_email(first_name, email):
  import smtplib
  gmail_user = "psetbuddy2021@gmail.com" # (You should provide your gmail account name)
  gmail_pwd = "testbuddy2021" # (You should provide your gmail password)
  smtpserver = smtplib.SMTP("smtp.gmail.com",587)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo
  smtpserver.login(gmail_user, gmail_pwd)
  subject = "Sorry!"
  to = email
  msg = "Hi " + first_name + ", \n\n" + "Unfortunately, we have some bad news... \n\n Our algorithms have been working hard while you were studying away, but there was not enough people who signed up for your class. Therefore we have not been able to find you any PSET buddies. \n\n Good luck on your studying! \n\n Best, \n\n The PSETBuddy Team"
  body = "Subject: {}\n\n{}".format(subject, msg)
  smtpserver.sendmail(gmail_user, to, body)
  smtpserver.close()

def feedback_email(request):
  if request.method == "POST":
    new_feedback = NewFeedbackForm(request.POST)
    new_feedback.save()
    import smtplib
    first_name = request.POST.get('first_name')
    email = request.POST.get('email')
    feedback = request.POST.get('feedback')


    # Send feedback email to ourselves
    gmail_user = "psetbuddy2021@gmail.com" # (You should provide your gmail account name)
    gmail_pwd = "testbuddy2021" # (You should provide your gmail password)
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    subject = "User Feedback"
    to = "psetbuddy2021@gmail.com"
    msg =  "Feedback: \n\n" + feedback
    body = "Subject: {}\n\n{}".format(subject, msg)
    smtpserver.sendmail(gmail_user, to, body)
    smtpserver.close()

    # Send feedback confirmation email to sender 
    gmail_user = "psetbuddy2021@gmail.com" # (You should provide your gmail account name)
    gmail_pwd = "testbuddy2021" # (You should provide your gmail password)
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    subject = "Thanks for providing feedback!"
    to = email
    msg =  "Hi " + first_name + ",\n\n Thank you for providing us with feedback on PSETBuddy! \n We will review your feedback and use it to improve psetbuddy.com.\n\n" + "Best, \n\n" + "The PSETBuddy Team" 
    body = "Subject: {}\n\n{}".format(subject, msg)
    smtpserver.sendmail(gmail_user, to, body)
    smtpserver.close()
  
    return redirect("/feedback.html")

    

def addbuddy(request):
  context = {}
  context["new_buddy_form"] = NewBuddyForm()
  return render(request, "services.html", context)



