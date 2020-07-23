import base64
import os
import json
import googleapiclient.discovery
from google.cloud import dns

ProjectId = os.environ.get('ProjectID')
ZoneName= os.environ.get('Private_Zone_Name')
DNSName = os.environ.get('DNS_name')

#data = '{"insertId":"dljq86dn4km", "logName":"projects/winter-form-254618/logs/cloudaudit.googleapis.com%2Factivity","operation":{"id":"operation-1595403163215-5ab02bed1275e-413127fd-a7a69663","last":true,"producer":"compute.googleapis.com"}, "protoPayload":{"@type":"type.googleapis.com/google.cloud.audit.AuditLog", "authenticationInfo":{"principalEmail":"acheq.rhermini@gmail.com"},"methodName":"v1.compute.instances.start","request":{"@type":"type.googleapis.com/compute.instances.start"},"requestMetadata":{"callerIp":"176.176.74.253","callerSuppliedUserAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36,gzip(gfe),gzip(gfe)"},"resourceName":"projects/winter-form-254618/zones/us-central1-a/instances/instance-2","serviceName":"compute.googleapis.com"},"receiveTimestamp":"2020-07-22T07:32:55.17164028Z","resource":{"labels":{"instance_id":"1625421287170767075","project_id":"winter-form-254618","zone":"us-central1-a"},"type":"gce_instance"},"severity":"NOTICE","timestamp":"2020-07-22T07:32:54.44Z"}'

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


def get_Inst_Name(data):
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
    return Inst_Res




def hello_pubsub(event, context):
    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))
    #print(event)
    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
        data_json = json.dumps(name, separators=(',', ':'))
        print(data_Json['resourceName'],data_Json['operation'])
        #Inst_Name=data_Json.

        #Inst_IP_Ad=

    else:
        name = 'World'
    #print(event['data'])
    #print('Hello {}!'.format(name))
    #print(list_resource_records(ProjectId,ZoneName))
    #Add_records(ProjectId,ZoneName,)
if __name__ == "__main__":
    data_to_parse = '{"insertId":"dljq86dn4km", "logName":"projects/winter-form-254618/logs/cloudaudit.googleapis.com%2Factivity","operation":{"id":"operation-1595403163215-5ab02bed1275e-413127fd-a7a69663","last":true,"producer":"compute.googleapis.com"}, "protoPayload":{"@type":"type.googleapis.com/google.cloud.audit.AuditLog", "authenticationInfo":{"principalEmail":"acheq.rhermini@gmail.com"},"methodName":"v1.compute.instances.start","request":{"@type":"type.googleapis.com/compute.instances.start"},"requestMetadata":{"callerIp":"176.176.74.253","callerSuppliedUserAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36,gzip(gfe),gzip(gfe)"},"resourceName":"projects/winter-form-254618/zones/us-central1-a/instances/instance-2","serviceName":"compute.googleapis.com"},"receiveTimestamp":"2020-07-22T07:32:55.17164028Z","resource":{"labels":{"instance_id":"1625421287170767075","project_id":"winter-form-254618","zone":"us-central1-a"},"type":"gce_instance"},"severity":"NOTICE","timestamp":"2020-07-22T07:32:54.44Z"}'
    print(get_Inst_Name(data_to_parse)[2])





