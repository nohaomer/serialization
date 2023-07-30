
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("pythonfirebase-16d86-firebase-adminsdk-zh4as-a918b6c88c.json")
firebase_admin.initialize_app(cred)
db = firestore.client()



#adding first data
# doc_ref = db.collection('employee').document('empdoc')
#
# doc_ref.set({
#
#     'name':'Parwiz',
#     'lname':'Forogh',
#     'age':24
#
#
# })
#adding second data
# doc_ref = db.collection('employee').document('emptwodoc')
# doc_ref.set({
#
#     'name':'John',
#     'lname':'Doe',
#     'email':'john@gmail.com',
#     'age':24
#
#
# })



#Reading the data


emp_ref = db.collection('employee')
docs = emp_ref.stream()

for doc in docs:
    print('{} => {} '.format(doc.id, doc.to_dict()))
