import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from twilio.rest import Client

cred = credentials.Certificate("C:/Users/Hp/PycharmProjects/pygui/robot-flutter-firebase-firebase-adminsdk-m3ffl-9f7f472f86.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('ambulance').document('LYqnMN8RbfUzkXEexO00')
doc = doc_ref.get()

if doc.exists:
    address = doc.get('address')





def ambulance():
    client = Client("AC60f4ecd35ed76890d2c3ed07a2e44177", "68ef144fba831210bc3ef526a9e2bc07")

    client.messages.create(to=("+8801793869255"), from_="+16073095689",
                           body=f"We need an emergency ambulance. A patient is sick. Address: {address}, "
                                f"Phone: ")
    print("Messege sent")



