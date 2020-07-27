import base64
import os
import json
import googleapiclient.discovery
from google.cloud import dns

PROJECT_ID = os.environ.get("PROJECT_ID")
DNS_ZONE_NAME= os.environ.get("DNS_ZONE_NAME")
DNS_SUF_ZONE=os.environ.get("DNS_SUF_ZONE")


def hello_pubsub(event, context):

    print("""This Function was triggered by messageId {} published at {}""".format(context.event_id, context.timestamp))
    
    if 'data' in event:
        data=base64.b64decode(event['data']).decode('utf-8')
        data_json = json.loads(data)
        protoPayload = data_json.get("protoPayload")
        resourceName = protoPayload.get("resourceName")
        resourceName = resourceName.split("/")
        project_name =resourceName[1]
        zone_name=resourceName[3]
        instance_name= resourceName[5]

        compute =googleapiclient.discovery.build('compute', 'v1', cache_discovery=False)
        instance = compute.instances().get(project=PROJECT_ID,zone=zone_name,instance=instance_name).execute()
        network_ip= instance.get("networkInterfaces")[0]
        instance_ip = network_ip.get("networkIP")
        
        client = dns.Client(project=PROJECT_ID)
        zone = client.zone(DNS_ZONE_NAME)
        TWO_HOURS = 2 * 60 * 60  # seconds
        elif:
             
        record_set = zone.resource_record_set(instance_name + DNS_SUF_ZONE ,'A', TWO_HOURS,instance_ip)
        changes = zone.changes()
        changes.add_record_set(record_set)
        changes.create() 

    else:
        print('no data in event')