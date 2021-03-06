import base64
import os
import json
#import googleapiclient.discovery

PROJECT_ID = os.environ.get('ProjectID')
ZONE_NAME  = os.environ.get('Private_Zone_Name')
DNS_NAME   = os.environ.get('DNS_name')


def list_resource_records(project_id, zone_name):
    client = dns.Client(project=project_id)
    zone = client.zone(zone_name)
    records = zone.list_resource_record_sets()
    return [(record.name, record.record_type, record.ttl, record.rrdatas) for record in records]
 
def add_records(project_id,zone_name,instance_name,instance_ip):
    client = dns.Client(project=project_id)
    zone = client.zone(zone_name)
    tow_hours = 2 * 60 * 60  # seconds
    record_set = zone.resource_record_set(instance_name +'.rhermini.com.','A', tow_hours ,instance_ip)
    changes = zone.changes()
    changes.add_record_set(record_set)
    changes.create() 


def get_instance_info(data):
    response=[]
    data_json = json.loads(data)
    protoPayload = data_json.get("protoPayload")
    resourceName = protoPayload.get("resourceName")
    resourceName = resourceName.split("/") # < type str > 
    project_name =resourceName[1]
    response.append(project_name)
    zone_name=resourceName[3]
    response.append(zone_name)
    instance_name= resourceName[5]
    response.append(instance_name)    
    return response
    
def get_instance_ip():
    network_ip= { 
        "networkInterfaces": {     
            "network": "https://www.googleapis.com/compute/v1/projects/winter-form-254618/global/networks/default",
            "subnetwork": "https://www.googleapis.com/compute/v1/projects/winter-form-254618/regions/us-central1/subnetworks/default",
            "networkIP": "10.128.0.8",
            "name": "nic0"
      }
      }
    network_ip= network_ip.get("networkInterfaces")
    network_ip=network_ip.get("networkIP")
    return network_ip


def hello_pubsub(event, context):
    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))
    #print(event)
    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'No data in event'
