from django.shortcuts import render
from .models import doctors,patients,feedbacks,messages
from django.db import connection
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector
import json
import re
# Create your views here.

def home(request):
    return render(request,'home.html')

#admin functionality

def admin(request):
    return render(request,'admin.html')

def adm_login(request):
    username=request.GET['username']
    passw=request.GET['password']
    if username!='admin' or passw!='admin':
        return render(request,'admin.html',{"data":'username or password incorrect'})
    else: 
       return render(request,'adminH.html',{"data":'login successfull'})
def backad(request):
    return render(request,'adminH.html')
def adminlogout(request):
    return render(request,'home.html')

def add(request):
    return render(request,'add_doc.html')
     
def doc_add(request):
    doc_name=request.GET['name']
    phone_num=request.GET['phone']
    special=request.GET['special']
    email=request.GET['email']
    password=request.GET['password']
    print(doc_name)
    if doc_name=="" or phone_num=="" or special=="" or email=="" or password=="":
        return render(request,'add_doc.html',{'data':'please enter correct data'})
    else:
        #print("INSERT INTO `health_prediction_doctor_data`(`name`, `email`, `password`, `specialization`, `phone_num`) VALUES('"+doc_name+"','"+email+"',"+password+",'"+special+"',"+phone_num+")")
       connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
       cursor=connection.cursor()
       cursor.execute("INSERT INTO `health_doctors`(`name`, `email`, `password`,  `phone_num`,`specialization`) VALUES('"+doc_name+"','"+email+"','"+password+"',"+phone_num+",'"+special+"')" )
       connection.commit()
       cursor.close()
       #addDoc=doctors(doc_name,email,password,special,phone_num,)
       #addDoc.save()
       return render(request,'add_doc.html',{"data":'entered new doctor'})
    

def doc_data(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `health_doctors` ')
    docData=cursor.fetchall()
    cursor.close()
    #docData=doctors.objects.all()
    return render(request,'doctor_data.html',{"doctors":docData} )

def patient_data(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM `health_patients` ')
    patientData=cursor.fetchall()
    cursor.close()
    #patientData=patients.objects.all()
    return render(request,'patient_data.html',{"patients":patientData} )

def feedback(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute('SELECT feedbackmsg FROM `health_feedbacks`')
    feedbacks=cursor.fetchall()

    #print(feedbacks)
    cursor.close()
    #feedbacks=feedbacks.objects.all()
    return render(request,'feedback.html',{"feedbacks":feedbacks} )

def deleterowofP(request):
    rowid=request.GET['rowid']
    #print(rowid)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    #print("DELETE FROM `health_patients` WHERE 'id'="+rowid)
    cursor.execute("DELETE FROM `health_patients` WHERE id="+rowid)
    connection.commit()
    cursor.execute("SELECT * FROM `health_patients`")
    patients=cursor.fetchall()
    cursor.close()
    return render(request,'adminH.html',{'patients':patients})
def deleterowofD(request):
    rowid=request.GET['rowid']
    print(rowid)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("DELETE FROM `health_doctors` WHERE id="+rowid)
    connection.commit()
    cursor.execute("SELECT * FROM `health_doctors`")
    doctors=cursor.fetchall()
    print(doctors)
    cursor.close()
    return render(request,'adminH.html',{'doctors':doctors})
def deleterowofF(request):
    rowid=request.GET['rowid']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("DELETE FROM `health_feedbacks` WHERE id="+rowid)
    connection.commit()
    cursor.execute("SELECT feedbackmsg FROM `health_feedbacks`")
    feedbacks=cursor.fetchall()
    cursor.close()
    return render(request,'adminH.html',{'feedbacks':feedbacks})
@csrf_exempt
def adddoctordata(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    phone=request.POST['phone']
    special=request.POST['specialist']
    #print(name,email)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    print("INSERT INTO `health_doctors`(`name`, `email`, `password`, `phonenum`,`specialization`) VALUES ('"+name+"','"+email+"','"+password+"',"+phone+",'"+special+"')")
    cursor.execute("INSERT INTO `health_doctors`(`name`, `email`, `password`, `phonenum`,`specialization`) VALUES ('"+name+"','"+email+"','"+password+"',"+phone+",'"+special+"')")
    connection.commit()
    cursor.execute("SELECT * FROM `health_doctors`")
    doctors=cursor.fetchall()
    cursor.close()
    print(doctors)
    return render(request,'adminH.html',{'doctors':doctors})
@csrf_exempt
def addpatientdata(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    phone=request.POST['phone']
    print(name)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO `health_patients`(`name`, `email`, `password`,`phonenum`) VALUES ('"+name+"','"+email+"','"+password+"',"+phone+")")
    connection.commit()
    cursor.execute("SELECT * FROM `health_patients`")
    patients=cursor.fetchall()
    cursor.close()
    return render(request,'adminH.html',{'patients':patients})
def getdoctordata(request):
    id=request.GET['doctorid']
    #print(id)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT `name`, `email`, `password`, `phonenum`, `specialization` FROM `health_doctors` WHERE id="+id)
    doctordata=cursor.fetchall()
    doctordata=doctordata[0]
    print(doctordata)
    cursor.close()
    #return render(request,'doctor_data.html',{"doctordata":doctordata})
    data=json.dumps(doctordata)
    return HttpResponse(data)
def getpatientdata(request):
    id=request.GET['patientid']
    print(id)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT `name`, `email`, `password`, `phonenum`, `status` FROM `health_patients` WHERE id="+id)
    patientdata=cursor.fetchall()
    patientdata=patientdata[0]
    print(patientdata)
    cursor.close()
    #return render(request,'patient_data.html',{"patientdata":patientdata})
    data=json.dumps(patientdata)
    return HttpResponse(data)
def editdoctordata(request):
    id=request.GET['doctorid']
    name=request.GET['name']
    password=request.GET['password']
    phone=request.GET['phone']
    specialist=request.GET['specialist']
    email=request.GET['email']
    #match = re.match(r'^\+?1?\d{10,11}$', phone)
    #if match is None:
    #    return render(request,'doctor_data.html',{"alert":'please add proper data'}) 
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("UPDATE `health_doctors` SET `name`='"+name+"',`email`='"+email+"',`password`='"+password+"',`phonenum`="+phone+",`specialization`='"+specialist+"' WHERE id="+id)
    connection.commit()
    cursor.execute("SELECT * FROM `health_doctors`")
    docData=cursor.fetchall()
    #user=userdata.objects.get(email=email) 
    #print(user)
    cursor.close()
    return render(request,'doctor_data.html',{"doctors":docData} )
def editpatientdata(request):
    id=request.GET['patientid']
    name=request.GET['name']
    password=request.GET['password']
    phone=request.GET['phone']
    status=request.GET['status']
    email=request.GET['email']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("UPDATE `health_patients` SET `name`='"+name+"',`email`='"+email+"',`password`='"+password+"',`phonenum`="+phone+",`status`='"+status+"' WHERE id="+id)
    connection.commit()
    cursor.execute("SELECT * FROM `health_patients`")
    patientData=cursor.fetchall()
    #user=userdata.objects.get(email=email) 
    #print(user)
    print(patientData)
    cursor.close()
    return render(request,'patient_data.html',{"patients":patientData} )
#patient functionality

def patient(request):
    try:
        email=request.session['pemail']
        connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM `health_patients` WHERE email='"+email+"'")
        patient=cursor.fetchall()
        print(patient)
        return render(request,'patient_profile1.html',{"patient":patient[0]})
    except: 
        return render(request,'patient.html')

def user_signup(request):
    return render(request,'patient_signup.html')


@csrf_exempt
def validate(request):
    username=request.POST['username']
    passw=request.POST['password']
    
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `health_patients` WHERE name='"+username+"' and password='"+passw+"'")
    patient=cursor.fetchall()
    #print("SELECT * FROM `health_prediction_patient_data` WHERE name='"+username+"' and password='"+passw+"'")
    #validation=patients(username,password)
    #validation.
    #print(patient)
    if len(patient)==0:
        return render(request,'patient.html',{"data":'username or password incorrect'})
    else:
        patient=patient[0]
        request.session['pemail']=patient[2]
        #print(patient[2])
        #score=0
        return render(request,'patient_profile1.html',{"patient":patient})
    #cursor.close()'''
    #return render(request,'patient_profile1.html')
def patientlogout(request):
    if request.session.has_key('pemail'):
        del request.session['pemail']
    return render(request,'patient.html')
def backp(request):
    id=request.GET['id']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `health_patients` WHERE id="+id)
    patient=cursor.fetchall()
    print(patient)
    patient=patient[0]
    return render(request,'patient_profile1.html',{"patient":patient})      
def back(request):
    return render(request,'home.html') 

def newAccount(request):
    patientName=request.POST['username']
    email=request.POST['email']
    password=request.POST['password']
    phone=request.POST['phone']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    match = re.match(r'^\+?1?\d{10,11}$', phone)
    if match is None:
        return render(request,'patient_signup.html',{"alert":'please add proper data'}) 
    else:
        connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
        cursor=connection.cursor()

        print("INSERT INTO `health_patients`(`name`, `email`, `password`,`phonenum`) VALUES ('"+patientName+"','"+email+"',"+password+","+phone+")")
        cursor.execute("INSERT INTO `health_patients`(`name`, `email`, `password`, `phonenum`) VALUES ('"+patientName+"','"+email+"',"+password+","+phone+")")
        connection.commit()
        return render(request,'patient.html',{"data":'signup successfull'})
def backpatient(request):
    patientid=request.GET['patientid']
    print(patientid)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT `name`, `email`, `password`,`phonenum`,`status` FROM `health_patients` where id='"+patientid+"'")
    a=cursor.fetchall()
    patient=[patientid]
    for i in a[0]:
        patient.append(i)
    print(patient)
    return render(request,'patient_profile1.html',{"patient":patient})
def msgP(request):
    doctorid=request.GET['doctorid']
    patientid=request.GET['patientid']
    #score=request.GET['score']
    #print(score)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT `id`,`name` FROM `health_doctors`")
    doctordatas=cursor.fetchall() 
    cursor.execute("SELECT * FROM `health_messages` where patientid='"+patientid+"'")
    queries=cursor.fetchall() 
    #print(doctordatas) 
    cursor.close()
    #print(queries)          
    return render(request,'messageP.html',{"doctordatas":doctordatas,"patientid":patientid,'queries':queries,'docid':doctorid})
def sendmsgP(request):
    doctorid=request.GET['doctorid']
    patientid=request.GET['patientid']
    msg=request.GET['msg']
    #print(doctorid,patientid,msg)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO `health_messages`(`doctorid`, `patientid`, `message`) VALUES ("+doctorid+","+patientid+",'"+msg+"')")
    connection.commit()
    cursor.execute("SELECT * FROM `health_messages` WHERE doctorid="+doctorid+" and patientid="+patientid)
    queries=cursor.fetchall()
    #print(msgdata)
    cursor.execute("SELECT `id`,`name` FROM `health_doctors`")
    doctordatas=cursor.fetchall() 
    #print(msgdata)
    cursor.close()
    return render(request,'messageP.html',{"queries":queries,"doctordatas":doctordatas,'docid':doctorid})
def updatepatient(request):
    email=request.session['pemail']
    name=request.GET['name']
    password=request.GET['password']
    phone=request.GET['phone']
    #score=request.GET['score']
    print(email)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("UPDATE `health_patients` SET `name`='"+name+"',`password`='"+password+"',`phonenum`="+phone+" WHERE `email`='"+email+"'")
    connection.commit()
    cursor.execute("SELECT * FROM `health_patients` WHERE `email`='"+email+"'")
    patient=cursor.fetchone()
    #print(patient)
    #user=userdata.objects.get(email=email) 
    #print(user)
    cursor.close()
    return render(request,'patient_profile1.html',{"patient":patient})
def questionanswer(request):
    email=request.session['pemail']
    patientid=request.GET['patientid']
    #print(email)
    return render(request,'questions.html',{'email':email,'patientid':patientid})
def updatestatuspatient(request):
    status=request.GET['status']
    email=request.GET['email']
    #score=request.GET['score']
    print(status)
    print(email)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    print("UPDATE 'health_patients' SET 'status'='"+status+"' WHERE `email`='"+email+"'")
    cursor.execute("UPDATE `health_patients` SET `status`='"+status+"' WHERE email='"+email+"'")
    connection.commit()
    cursor.execute("SELECT * FROM `health_patients` WHERE `email`='"+email+"'")
    patient=cursor.fetchone()
    cursor.close()
    return render(request,'patient_profile1.html',{"patient":patient})
def patientfeedback(request):
    patientid=request.GET['patientid']
    email=request.GET['email']
    print(email)
    return render(request,'feedbackP.html',{"patientid":patientid}) 
def addfeedback(request):
    email=request.session['pemail']
    feedback=request.GET['feedbackP']
    print(email,feedback)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("INSERT INTO `health_feedbacks`( `feedbackmsg`) VALUES ('"+feedback+"')")
    connection.commit()
    cursor.execute("SELECT * FROM `health_patients` WHERE `email`='"+email+"'")
    patient=cursor.fetchone()
    cursor.close()

    return render(request,'patient_profile1.html',{'patient':patient})



#doctor functionality

def doctor(request):
    
    try:
        email=request.session['demail']
        connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM `health_doctors` WHERE email='"+email+"'")
        doctor=cursor.fetchone()
        print(doctor)
        return render(request,'doctor_profile.html',{"doctor":doctor})
    except: 
        return render(request,'doctor.html')

@csrf_exempt
def doctorlogin(request):
    name=request.POST['username']
    password=request.POST['password']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `health_doctors` WHERE name='"+name+"' and password='"+password+"'")
    doctor=cursor.fetchall()
    #print(doctor)
    if len(doctor)==0:
        #print('y')
        return render(request,'doctor.html',{"data":'username or password incorrect'})
    else:
        doctor=doctor[0]
        request.session['demail']=doctor[2]
        #print(doctor[2])
        return render(request,'doctor_profile.html',{"doctor":doctor})
def backd(request):
    id=request.GET['doctorid']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `health_doctors` WHERE id="+id)
    doctor=cursor.fetchall()
    print(doctor)
    doctor=doctor[0]
    return render(request,'doctor_profile.html',{"doctor":doctor})
'''def backdoctor(request):
    doctorid=request.GET['doctorid']
    print(doctorid)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT  `name`, `email`, `password`, `phonenum`, `specialization` FROM `health_doctors` WHERE id='"+doctorid+"'")
    a=cursor.fetchall()
    doctor=[doctorid]
    for i in a[0]:
        doctor.append(i)
    print(doctor)
    return render(request,'doctor_profile.html',{"doctor":doctor})'''
def msgD(request):
    doctorid=request.GET['doctorid']
    #print(doctorid)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("SELECT `id`,`message`,`replay` FROM `health_messages` WHERE doctorid="+doctorid)
    #cursor.execute("SELECT `id`,`name` FROM `health_patients`")
    messagedata=cursor.fetchall() 
    
    #print(messagedata)   
    cursor.close()            
    return render(request,'messageD.html',{"messagedata":messagedata,"doctorid":doctorid})
def rplymsg(request):
    msg=request.GET['msg']
    messageid=request.GET['messageid']
    doctorid=request.GET['doctorid']
    #print(doctorid,messageid,msg)
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("UPDATE `health_messages` SET `replay`='"+msg+"' WHERE id="+messageid)
    connection.commit()
    #print("SELECT `id`,`message`,`replay` FROM `health_messages` WHERE doctorid="+doctorid)
    cursor.execute("SELECT `id`,`message`,`replay` FROM `health_messages` WHERE doctorid="+doctorid)
    messagedata=cursor.fetchall() 
    print(messagedata)   
    cursor.close()            
    return render(request,'messageD.html',{"messagedata":messagedata,"doctorid":doctorid})
def displaymsg(request):
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM  `health_messages` where doctor')

def updatedoctordata(request):
    name=request.GET['name']
    password=request.GET['password']
    phone=request.GET['phone']
    specialist=request.GET['specialist']
    email=request.session['demail']
    connection=mysql.connector.connect(host='localhost',user='root',password='',database='healthprediction')
    cursor=connection.cursor()
    cursor.execute("UPDATE `health_doctors` SET `name`='"+name+"',`password`='"+password+"',`phonenum`="+phone+",`specialization`='"+specialist+"' WHERE email='"+email+"'")
    connection.commit()
    cursor.execute("SELECT * FROM `health_doctors` WHERE email='"+email+"'")
    doctor=cursor.fetchone()
    #user=userdata.objects.get(email=email) 
    #print(user)
    cursor.close()
    return render(request,'doctor_profile.html',{"doctor":doctor})

def doctorlogout(request):
    if request.session.has_key('demail'):
        del request.session['demail']
    return render(request,'doctor.html')
     

