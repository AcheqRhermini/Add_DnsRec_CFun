import base64
import os
import json
import googleapiclient.discovery
from google.cloud import dns

ProjectId = os.environ.get('ProjectID')
DnsPrivateZoneName= os.environ.get('Private_Zone_Name')
DNSName = os.environ.get('DNS_name')
ZoneName = os.environ.get('Zone_Name')

###### Methode pour récuperer, sous forme de liste, le nom de l'instance ; l'adresse ip de l'instance.      
def get_instance_info(data):
    response=[]
    data_json = json.loads(data)
    protoPayload = data_json.get("protoPayload")
    resourceName = protoPayload.get("resourceName")
    resourceName = resourceName.split("/")
    project_name =resourceName[1]
    response.append(project_name)
    zone_name=resourceName[3]
    response.append(zone_name)
    instance_name= resourceName[5]
    response.append(instance_name)    
    return response

def get_instance_ip():
    with open('out.json') as f:
        network_ip = json.load(f)
        network_ip= network_ip.get("networkInterfaces")[0]
        network_ip = network_ip.get("networkIP")
    return network_ip

   
def list_resource_records(project_id, dns_zone_name):
    client = dns.Client(project=project_id)
    zone = client.zone(dns_zone_name)
    records = zone.list_resource_record_sets()
    return [(record.name, record.record_type, record.ttl, record.rrdatas) for record in records]


def Add_records(project_id,dns_zone_name,instance_name,instance_ip):
    client = dns.Client(project=project_id)
    zone = client.zone(dns_zone_name)
    two_hours = 2 * 60 * 60  # seconds
    record_set = zone.resource_record_set(instance_name +instance_name,'A', two_hours, instance_ip)
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



