import base64
import os
import json
import googleapiclient.discovery
from google.cloud import dns

ProjectId = os.environ.get('ProjectID')
ZoneName= os.environ.get('Private_Zone_Name')
DNSName = os.environ.get('DNS_name')

###### Methode pour récuperer, sous forme de liste, le nom de l'instance ; l'adresse ip de l'instance.      
def get_Inst_Info(data):
    Inst_Res=[]
    data_json = json.loads(data)
    data_json=json.dumps(data_json['protoPayload'])
    data_json=json.loads(data_json)
    Inst_info = data_json['resourceName']
    Inst_info = Inst_info.split("/")
    Project_Name=Inst_info[1]
    Inst_Res.append(Project_Name)
    Zone_name=Inst_info[3]
    Inst_Res.append(Zone_name)
    Inst_Name=Inst_info[5]
    Inst_Res.append(Inst_Name)
    Inst_Add = compute.instances().get(ProjectId,ZoneName ,Inst_Name).execute()
    Inst_Add= json.loads(Inst_Add)
    Inst_Add= json.dumps(Inst_Add['networkInterfaces'])
    Inst_Add= json.loads(Inst_Add)
    Inst_Add= json.dumps(Inst_Add[0])
    Inst_Add= json.loads(Inst_Add)
    Inst_Add=Inst_Add['networkIP'] 
    Inst_Res.append(Inst_Add)
    return Inst_Res

   
def list_resource_records(project_id, zone_name):
    client = dns.Client(project=project_id)
    zone = client.zone(zone_name)
    records = zone.list_resource_record_sets()
    return [(record.name, record.record_type, record.ttl, record.rrdatas) for record in records]


def Add_records(project_id,zone_name,Ist_N,Ist_IP):
    client = dns.Client(project=project_id)
    zone = client.zone(zone_name)
    TWO_HOURS = 2 * 60 * 60  # seconds
    record_set = zone.resource_record_set(Ist_N +'.rhermini.com.','A', TWO_HOURS,Ist_IP)
    changes = zone.changes()
    changes.add_record_set(record_set)
    changes.create() 


def hello_pubsub(event, context):
    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))
    #print(event)
    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'World'
    print('Hello {}!'.format(name))
    Inst_Name=get_Inst_Info(name)[2]
    Inst_IP=get_Inst_Info(name)[3]
    Instance_name = get_Inst_Info(data_to_parse)[2]
    Instance_Address = get_Inst_Info[3]
    Add_records(ProjectId,ZoneName,Inst_Name,Inst_IP)