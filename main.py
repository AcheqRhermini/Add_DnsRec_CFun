import base64
import os
import json
import googleapiclient.discovery
from google.cloud import dns

ProjectId = os.environ.get('ProjectID')
ZoneName= os.environ.get('Private_Zone_Name')
DNSName = os.environ.get('DNS_name')

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
        data_json = json.dumps(name, separators=(',', ':'))
        print(data_Json['resourceName'])
        #Inst_Name=data_Json.

        #Inst_IP_Ad=

    else:
        name = 'World'
    #print(event['data'])
    #print('Hello {}!'.format(name))
    #print(list_resource_records(ProjectId,ZoneName))
    #Add_records(ProjectId,ZoneName,)
