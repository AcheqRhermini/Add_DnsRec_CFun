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
    return Inst_Res
    
def get_Inst_Add(data):
    Inst_Add= json.load(f)
    Inst_Add= json.dumps(Inst_Add['networkInterfaces'])
    Inst_Add= json.loads(Inst_Add)
    Inst_Add= json.dumps(Inst_Add[0])
    Inst_Add= json.loads(Inst_Add)
    Inst_Add=Inst_Add['networkIP']
    return Inst_Add




def hello_pubsub(event, context):
    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))
    #print(event)
    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'World'
    #Inst_Name=get_Inst_Info(name)[2]
if __name__ == "__main__":
    data_to_parse = '{"insertId":"dljq86dn4km", "logName":"projects/winter-form-254618/logs/cloudaudit.googleapis.com%2Factivity","operation":{"id":"operation-1595403163215-5ab02bed1275e-413127fd-a7a69663","last":true,"producer":"compute.googleapis.com"}, "protoPayload":{"@type":"type.googleapis.com/google.cloud.audit.AuditLog", "authenticationInfo":{"principalEmail":"acheq.rhermini@gmail.com"},"methodName":"v1.compute.instances.start","request":{"@type":"type.googleapis.com/compute.instances.start"},"requestMetadata":{"callerIp":"176.176.74.253","callerSuppliedUserAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36,gzip(gfe),gzip(gfe)"},"resourceName":"projects/winter-form-254618/zones/us-central1-a/instances/instance-2","serviceName":"compute.googleapis.com"},"receiveTimestamp":"2020-07-22T07:32:55.17164028Z","resource":{"labels":{"instance_id":"1625421287170767075","project_id":"winter-form-254618","zone":"us-central1-a"},"type":"gce_instance"},"severity":"NOTICE","timestamp":"2020-07-22T07:32:54.44Z"}'
    out_request = {
  "id": "4782489585701298563",
  "creationTimestamp": "2020-07-21T00:55:24.748-07:00",
  "name": "instance-6",
  "description": "",
  "tags": {
    "fingerprint": "42WmSpB8rSM="
  },
  "machineType": "https://www.googleapis.com/compute/v1/projects/winter-form-254618/zones/us-central1-a/machineTypes/n1-standard-1",
  "status": "TERMINATED",
  "zone": "https://www.googleapis.com/compute/v1/projects/winter-form-254618/zones/us-central1-a",
  "canIpForward": false,
  "networkInterfaces": [
    {
      "network": "https://www.googleapis.com/compute/v1/projects/winter-form-254618/global/networks/default",
      "subnetwork": "https://www.googleapis.com/compute/v1/projects/winter-form-254618/regions/us-central1/subnetworks/default",
      "networkIP": "10.128.0.8",
      "name": "nic0",
      "accessConfigs": [
        {
          "type": "ONE_TO_ONE_NAT",
          "name": "External NAT",
          "networkTier": "PREMIUM",
          "kind": "compute#accessConfig"
        }
      ],
      "fingerprint": "Oaza_AFcY8c=",
      "kind": "compute#networkInterface"
    }
  ],
  "disks": [
    {
      "type": "PERSISTENT",
      "mode": "READ_WRITE",
      "source": "https://www.googleapis.com/compute/v1/projects/winter-form-254618/zones/us-central1-a/disks/instance-6",
      "deviceName": "instance-6",
      "index": 0,
      "boot": true,
      "autoDelete": true,
      "licenses": [
        "https://www.googleapis.com/compute/v1/projects/cos-cloud-shielded/global/licenses/shielded-cos",
        "https://www.googleapis.com/compute/v1/projects/cos-cloud/global/licenses/cos",
        "https://www.googleapis.com/compute/v1/projects/cos-cloud/global/licenses/cos-pcid"
      ],
      "interface": "SCSI",
      "guestOsFeatures": [
        {
          "type": "UEFI_COMPATIBLE"
        },
        {
          "type": "SECURE_BOOT"
        },
        {
          "type": "VIRTIO_SCSI_MULTIQUEUE"
        },
        {}
      ],
      "diskSizeGb": "10",
      "shieldedInstanceInitialState": {
        "pk": {
          "content": "MIIEfTCCA2WgAwIBAgIJAKUErrp7YQApMA0GCSqGSIb3DQEBCwUAMIGFMQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLR29vZ2xlIExMQy4xFDASBgNVBAsTC0Nocm9taXVtIE9TMR0wGwYDVQQDExRVRUZJIFBsYXRmb3JtIEtleSB2MTAeFw0xODEyMDgwMTE5NDBaFw0yODEyMDUwMTE5NDBaMIGFMQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLR29vZ2xlIExMQy4xFDASBgNVBAsTC0Nocm9taXVtIE9TMR0wGwYDVQQDExRVRUZJIFBsYXRmb3JtIEtleSB2MTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAL5uKpSnDVAfJWeiQ1MlHJtRONJeyRsENEPZNj_Cu3GgVLJ6UP4IW3YCvu0WhjsQu2uoiDh6Ae1KOonhF27r7e01O9ZyRy-Cx64qJRYnwBBNqRVT0LoWzzS1b0K4KpAeXvWur3E6MM5yOJEOY12durNRfOCIjCG11-o7WWpS4Bs_uSkKy2aNvuK2JqJFtD5etn44gLRcymUjifPXMGBAFIxyTo_CR7VQcmBi3RYjzM90-D5BwxV9hGga5Mhrj8-VkHGri1odtlrNVcG_6Q8ROsplTAEWDX1ZPfhu7A_1gkJZfovPoyn2d0Z4L0GiU_hrynQUA-pnFpuKQmPqXfUUQcMCAwEAAaOB7TCB6jAdBgNVHQ4EFgQU3OLwrM30GgWfO1aUEix9FQjn1_wwgboGA1UdIwSBsjCBr4AU3OLwrM30GgWfO1aUEix9FQjn1_yhgYukgYgwgYUxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtHb29nbGUgTExDLjEUMBIGA1UECxMLQ2hyb21pdW0gT1MxHTAbBgNVBAMTFFVFRkkgUGxhdGZvcm0gS2V5IHYxggkApQSuunthACkwDAYDVR0TBAUwAwEB_zANBgkqhkiG9w0BAQsFAAOCAQEAEFGJ1Z36MRgmVgub6niwWjSGbpzKC_0l-o0zKJYWngnqOOp2O0YRb3sfm134xYmrChANnBkmiErJGYbgGuZFn9OoUZaYv41ZaGe8zpnFIBUnFLNq6mmtQWgo5jW2pdVe5L39UqB_rVkeE1eBHPeDgAhd-rkSNtSdRNgKtaE7Xc60PHqG-HOgwKE9X3rBFKM99JKs9v_wrJ_mMBCayk2QWCfjNFYBVz87rtFub7rDHOGGDqUYvUTLzYeP1-h3ziUlddByXpfN_AzHRxezCIDOlnnAW126TmhShErzq5Nq664nygzy5WZYEpsEkqKtHxMnbE42at25LbsvU-U4Vg2mbQ==",
          "fileType": "X509"
        },
        "keks": [
          {
            "content": "MIID9TCCAt2gAwIBAgIUajaVim_hVYORMrNb47Opztsf_A4wDQYJKoZIhvcNAQELBQAwgYkxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKDAtHb29nbGUgTExDLjEUMBIGA1UECwwLQ2hyb21pdW0gT1MxITAfBgNVBAMMGFVFRkkgS2V5IEV4Y2hhbmdlIEtleSB2MTAeFw0xOTA1MTAyMTE5MDlaFw0yOTA1MDcyMTE5MDlaMIGJMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNTW91bnRhaW4gVmlldzEUMBIGA1UECgwLR29vZ2xlIExMQy4xFDASBgNVBAsMC0Nocm9taXVtIE9TMSEwHwYDVQQDDBhVRUZJIEtleSBFeGNoYW5nZSBLZXkgdjEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDAHCnAIiJzIVqp8ZV74iQA6X8mvy3U_eQiwquED9b8yX12oorGyDWQWSnHX8htef5suHwhlTQ902gxQeqpRrno78Kwwxlg187BSBviJySF0BHyr858qHcywHA7gDGDV87xrsCCZ5nFIoLZOevfUOA1d4byewKNux2LbLOYYURcWC9pCeIrzlt5EmZ4PXM-W5L_YQ_isOQ3yYUpwkHt4TGfKsKamhmcD5RSWSWBlP8lvxRV6cbc4G8Tc05ZFh4TfYZn1akUHkh9AwQgfl79s6K6OwHFBekyotzkRvJcdNZrIamEJmPgCap6ftjO2z3N2eUNvAiWzLzae-92mO1VrJtpAgMBAAGjUzBRMB0GA1UdDgQWBBQ0zIgfPaMmxVZDyBWDGJ4K_i05RTAfBgNVHSMEGDAWgBQ0zIgfPaMmxVZDyBWDGJ4K_i05RTAPBgNVHRMBAf8EBTADAQH_MA0GCSqGSIb3DQEBCwUAA4IBAQBsYW2MYsQ-U3EIlBRiVFww0lNl-D1ePhqcAD2SMVNAXgsjcSVkWZsH4SRS2vP64z4bCHLd4qPfCBNJZUNb3eu0YHhDuz5rMJPDvH-nYP0DoB3Nl8v_I48DCv5Wn3AXSKzeMRy4RNZI_IReYh3yonFA6cX2nxBfR6d6QlUuS0ngFtQkgTEzFUs_aCrvfu-3gWhwclSBKEJv808Buhhg-1EzGeausmLBzwwmi7RaEIRtw-kDDP2d2-E00TWqN5RID6jfjUCzITrUuA45NXK2473f3X_u09iLfbNZkTmgd6tArNehy6N_4F3_3yT_Ixx0kKYfjnDHhuqJRz18Qt6sLNP0",
            "fileType": "X509"
          }
        ],
        "dbs": [
          {
            "content": "MIID9zCCAt-gAwIBAgIUW6do6zceodf8w_veGuL25bP6OmQwDQYJKoZIhvcNAQELBQAwgYoxCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKDAtHb29nbGUgTExDLjEfMB0GA1UECwwWQ29udGFpbmVyIE9wdGltaXplZCBPUzEXMBUGA1UEAwwOVUVGSSBEQiBLZXkgdjUwHhcNMjAwNzA4MTgwMjQ3WhcNMzAwNzA2MTgwMjQ3WjCBijELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExFjAUBgNVBAcMDU1vdW50YWluIFZpZXcxFDASBgNVBAoMC0dvb2dsZSBMTEMuMR8wHQYDVQQLDBZDb250YWluZXIgT3B0aW1pemVkIE9TMRcwFQYDVQQDDA5VRUZJIERCIEtleSB2NTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANAM2iTfuz8Ty6i5Hf4ZEbns69JT7tRjheNx6qqPPh7SoXo67s-aJD9cF4Q2zTmQWUzUqkryY5stWSdbw3Yq34bMoSl5ok3NI_TbY_UU9MEBgGl-IAoCF6msT-fmGaIYs7oI15E-NrZGOkWUjVpsxQK7Q1qjxoYhgxGEBKg_c7NyBnjGEAJpUMFpSYVVNnrwiTGldWdlgb9xZGsbGgzpx9vbqUFSSS0yPWWpQEYwrDNIpLmS_9C2JWvs1r9i8DFRuMYTWqIGy-eRrCSsPpWc7Q4ZMJjoEHxspcoyxXENM0Iz_XPBz8_4_TGXyrgMDCjvFN8YB75EWdz5_GSJPWAO7TcCAwEAAaNTMFEwHQYDVR0OBBYEFLXxtq-MtCMwgQdpSj4ssbLxlJh-MB8GA1UdIwQYMBaAFLXxtq-MtCMwgQdpSj4ssbLxlJh-MA8GA1UdEwEB_wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBALzSs5QlhEbLUo3hxCb9vzDLz5V8mweRPJe33j0FwMn789LHi5rpD8IDgr7MGbijTW48UqB6hhGmn8y_SMgqTNgRNrqQ--D6fyNItDx7n91nIdXjUwpOSaDD0-OUDy_siz91AmsRqP53m0dKm8yFiRTm3voaonD0QGFOb988cQY0xPHkg_d9zDGdcUYx3MbpTGZE2DtAtVIs4eaYsiiqCgmS6lQAz2AqMdHVeKeR8qev1HnEprkf7X-Ctr74mE_TC_WY_Kc4B5sW3BtX6ypYNBUe3vWJpuxo5G5XduhgCoHzH2Sy9p5fLzkll10HJ91mRjMFKwwFIKTJDds-m5Z69eE=",
            "fileType": "X509"
          }
        ],
        "dbxs": [
          {
            "content": "MIIEaDCCA1CgAwIBAgIJAKqfsrCdjyCoMA0GCSqGSIb3DQEBCwUAMH8xCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtHb29nbGUgTExDLjEUMBIGA1UECxMLQ2hyb21pdW0gT1MxFzAVBgNVBAMTDlVFRkkgREIgS2V5IHYxMB4XDTE4MTIwODAxMTk0MVoXDTI4MTIwNTAxMTk0MVowfzELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC0dvb2dsZSBMTEMuMRQwEgYDVQQLEwtDaHJvbWl1bSBPUzEXMBUGA1UEAxMOVUVGSSBEQiBLZXkgdjEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCtZ9U4P5aWlBwiTocmkUjOn2XpvHUlUOnsnhvsm994hAb0MNk2d3fXa8Nz14v9JiBTSf70KU2Zhxb_bSN3KAIv-f7F2AuXte7U9SnzZ02UDmK4TU1bFQW67Y3Gc2hWprCHYEjiRQD4J3WPWhuZnAXqzXQk3uDWVPETi-G9KAM1R-yNxZfoEjfIKhLabDsWqDtnMSovObLoVfwTdnm0WCuYTFtY_CKNxuxeKuzDsC5Su9N3dSFbpGhXJjwUaXPLWY5MFIqIQNBfhmWzDd4PItXaXV3V44IqWTXclE2aSUqkwNrEZ1cRpHG4PYM1aHVmjcO_dWlvthcepTIMIEMAXg2LAgMBAAGjgeYwgeMwHQYDVR0OBBYEFNXbmmdkM0aIsPMyEIv25JRaOPA-MIGzBgNVHSMEgaswgaiAFNXbmmdkM0aIsPMyEIv25JRaOPA-oYGEpIGBMH8xCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtHb29nbGUgTExDLjEUMBIGA1UECxMLQ2hyb21pdW0gT1MxFzAVBgNVBAMTDlVFRkkgREIgS2V5IHYxggkAqp-ysJ2PIKgwDAYDVR0TBAUwAwEB_zANBgkqhkiG9w0BAQsFAAOCAQEAJ2vbNymAKTUbRvxnAohHozVUByrKHCq1o8b-bKrgv7Ch0X4itfG8Uwvt0xG7CTpl_Dno92MtpOpFv4ydqox-pP1kTsRcnFNggndXdjpGILIB94KmFiYJvB6RzocJsXsXBa0tULOR24qiB9f93kfITS7Ec60WjFfpgYKEnuEgcV0yBuZzAZbxo1uF4n1hhmVUnKtEI9pX-8geYIIqIYiwwT2jnhFogWw4PeSyg-HMR1CLwwJeH2XDa924LpgHFuR-AbikipAE2vIE0yqJzo0o4tn9-sRuMaQcZ4VQqIzMiniW5H7nGeoQY3ktHX5eq6x-4jFvdLnzzq_D4sS-UWHzOA==",
            "fileType": "X509"
          },
          {
            "content": "MIIEiTCCA3GgAwIBAgIJAOzm3xz71Vu6MA0GCSqGSIb3DQEBCwUAMIGJMQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLR29vZ2xlIExMQy4xFDASBgNVBAsTC0Nocm9taXVtIE9TMSEwHwYDVQQDExhVRUZJIEtleSBFeGNoYW5nZSBLZXkgdjEwHhcNMTgxMjA4MDExOTQwWhcNMjgxMjA1MDExOTQwWjCBiTELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC0dvb2dsZSBMTEMuMRQwEgYDVQQLEwtDaHJvbWl1bSBPUzEhMB8GA1UEAxMYVUVGSSBLZXkgRXhjaGFuZ2UgS2V5IHYxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwg5hvVH6fJSBNji7ynBl1SQzWceL5P3ul6RcB-1s5wXqzXlIHiyRqBdj4hj2pLzpKJGmXWnerIwJOkdsFg7IwZpA4xHE1F-M8XlpuuUn_Xdfccef36ddZEUH6QLwNm96T89F4ujt0omJ-0GV37vBsxEY-hwR3O8XBgyx8TvvYxNnVyTgi19qQdb2ES8-yWJkebdzgugcmNf9K-55fnEiyxWtrvEQb2sowWIS3-b1I_BP85pW2pldh9yQWfb3OY2NJhGSbQSnLi3J0IhRXROEtAXCU4MLTq2cHOpGX0DtJP_g_jD1pnC1O6CCZgVycK4DgZXeDzOG_2Uimhr0y1rcewIDAQABo4HxMIHuMB0GA1UdDgQWBBQEqlpkrYWCzJe69eMUdF1byztBmzCBvgYDVR0jBIG2MIGzgBQEqlpkrYWCzJe69eMUdF1byztBm6GBj6SBjDCBiTELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC0dvb2dsZSBMTEMuMRQwEgYDVQQLEwtDaHJvbWl1bSBPUzEhMB8GA1UEAxMYVUVGSSBLZXkgRXhjaGFuZ2UgS2V5IHYxggkA7ObfHPvVW7owDAYDVR0TBAUwAwEB_zANBgkqhkiG9w0BAQsFAAOCAQEAWsd3mq0dADTD7Tx2uYcDeJcJHO0x91hO26p2cqUSox4wPgc4_xk5yiteMgDB5CWLwgcuneDAYYMO1PmktpEvLu9a82gCGxGiww-w78OJTOrs68VM1zB0jqA3X5EyVSwVJqi8idgrnnGsJAcSBosnUI8pNi9SDC3MRPE1q1EUjuDNjsE7t_ItBe-MSMWCH2hpG8unZ7uwWCRfAV3Fkdnq_S5HzDy6-kKyGdj-rprhVeDz2xSyMOlNIJig4uuqU166DTfoQA2TxnMG_TuHt69Z4uZcVwx_HwPs2-vUCCYqZDwuuHKNIEm8kIK8sSPSsp22sC8h-7Klb8wj_d0lzShgkg==",
            "fileType": "X509"
          },
          {
            "content": "MIID0zCCArugAwIBAgIJANuXsNG_1HHxMA0GCSqGSIb3DQEBCwUAMH8xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKDAtHb29nbGUgTExDLjEUMBIGA1UECwwLQ2hyb21pdW0gT1MxFzAVBgNVBAMMDlVFRkkgREIgS2V5IHYxMCAXDTE4MDQyNzE1MDYzN1oYDzIyMTgwMzEwMTUwNjM3WjB_MQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNTW91bnRhaW4gVmlldzEUMBIGA1UECgwLR29vZ2xlIExMQy4xFDASBgNVBAsMC0Nocm9taXVtIE9TMRcwFQYDVQQDDA5VRUZJIERCIEtleSB2MTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALWzFg8obysKXCjnbBTpAM8dMFC2pHX7GpwESNG-FYQI218Y1Ao1p5BttGqPoU5lGNeYUXxgxIqfN18ALHH10gRCRfqbC54faPU1lMr0e0jvi67GgGztyLl4ltAgK7HHTHmtZwghYNS45pKz_LFGm-TlKg-HPZBFT9GtbjRZe5IS2xdKkWM_sPA8qXwzvqmLN3OQckf0KchSUQmB3-wh4vYFV2TEjz10oR0FZO8LFFOOeooukcRDYy219XrdM21APnfszHmfKhzAFddOcYdwKwOL-w9TKVUwCIM70GL_YOtywA17mQkEm0ON79oyQ0daDlZ0ngDxC8xUIASYsRRPOkkCAwEAAaNQME4wHQYDVR0OBBYEFFO6MYgG9CvYp6qAqn_Jm-MANGpvMB8GA1UdIwQYMBaAFFO6MYgG9CvYp6qAqn_Jm-MANGpvMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAIGyOB_3oFo6f3WoFrdBzimb_weH8hejtCggpcL-8Wdex9VRl5MKi_1GlGbietMDsr1alwdaagam9RafuIQplohTSBnQrU-u-LbtRlCF9C25GDQ70S0QlxAQmt41Sc7kSFTPm6BHauF3b_Raf9AX30MamptoXoAhgMnHAitCn6yCOsRJ_d1t04lqsiqefhf26xItvRnkuxG7-IQnbyGFCGPcjFNAE1thLpL_6y_dprVwTLsvZnsWYj-1Gg1yUkOnCN8Kl3Q3RDVqo98mORUc0bKB-B8_FQsbtmzbb-29nXQJW1FJx0ejqJyDGGBPHAGpwEJTVB3mwWXzBU6Ny7T3dlk=",
            "fileType": "X509"
          },
          {
            "content": "MIID6TCCAtGgAwIBAgIJAKgdcZ45rGMDMA0GCSqGSIb3DQEBCwUAMIGJMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNTW91bnRhaW4gVmlldzEUMBIGA1UECgwLR29vZ2xlIExMQy4xFDASBgNVBAsMC0Nocm9taXVtIE9TMSEwHwYDVQQDDBhVRUZJIEtleSBFeGNoYW5nZSBLZXkgdjEwIBcNMTgwNDI3MTUwNjM3WhgPMjIxODAzMTAxNTA2MzdaMIGJMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNTW91bnRhaW4gVmlldzEUMBIGA1UECgwLR29vZ2xlIExMQy4xFDASBgNVBAsMC0Nocm9taXVtIE9TMSEwHwYDVQQDDBhVRUZJIEtleSBFeGNoYW5nZSBLZXkgdjEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCbIdHPMQZZU68jI5kz5rmwvo-DQZZJ5amRnAUnBpNllhNQB6TaLUS_D9TIo_0X1e8T21Xk4Pf3D5ckbuQxsJzQ5OVEOb59sJ9AhjVUoxQxuVW-iBzD0mWbxKf2cASy2YRIEcaAAI5QT2SwO8gZy_G8LwAk-vO0vIbynN0WuFLl1Dp2cMQ3CxLSPH-QPSZyGd6o6ewUU9JzboppujXpk43EQH5ZJE_wJb_ujUFWcFzKHb_EkV1hI1TmBJ1-vR2kao4_1hQO6k1zLUR-MyBHY0SRU2OQxBpSez-qt7oItMBc1EanXvq9tqx0ndCTmXQYQplT5wtkPbE9sd5zwbDt8btHAgMBAAGjUDBOMB0GA1UdDgQWBBS5Tmmv3JM8w1mfP9V5xAIdjBhb7TAfBgNVHSMEGDAWgBS5Tmmv3JM8w1mfP9V5xAIdjBhb7TAMBgNVHRMEBTADAQH_MA0GCSqGSIb3DQEBCwUAA4IBAQB9BRTP37ik4jF2BmJJspMA6NHS7mxIckFCYKl-TO8zGFd3mlA6dnEw5WY-tUcBNJpAaHNJV_rzagGPpWMIoy-nAaLSSpnyhEXYTnQvzejYRijN3N0V9tmM0qgViHNBqTxdfcwlst5OUesGHPqgBOt5RRu5OGJ0rkuymWwxHOKIw43hz5FW7vhumbtJ3iy8HSFQIjSYMkr0sOzJhmvnHlpZ4pOoPNyNA9DM6smriH-2-MnJFM9w8bg6zsV5X-6KL464_FuXL_X_IWmAsAbi8Ge8ZMJjEaDrF1qkD4aLvu0MshzEdvrvQO-3Gn3Lmi_RYKR0HKZp7jXTySj76sxt9QK4",
            "fileType": "X509"
          }
        ]
      },
      "kind": "compute#attachedDisk"
    }
  ],
  "metadata": {
    "fingerprint": "QGFpUP9iZI4=",
    "items": [
      {
        "key": "startup-script",
        "value": "apt-get update -y\napt-get install - y net-tools\napt-get intsall -y apache2"
      }
    ],
    "kind": "compute#metadata"
  },
  "serviceAccounts": [
    {
      "email": "667178863650-compute@developer.gserviceaccount.com",
      "scopes": [
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring.write",
        "https://www.googleapis.com/auth/servicecontrol",
        "https://www.googleapis.com/auth/service.management.readonly",
        "https://www.googleapis.com/auth/trace.append"
      ]
    }
  ],
  "selfLink": "https://www.googleapis.com/compute/v1/projects/winter-form-254618/zones/us-central1-a/instances/instance-6",
  "scheduling": {
    "onHostMaintenance": "MIGRATE",
    "automaticRestart": true,
    "preemptible": false
  },
  "cpuPlatform": "Unknown CPU Platform",
  "labelFingerprint": "42WmSpB8rSM=",
  "startRestricted": false,
  "deletionProtection": false,
  "reservationAffinity": {
    "consumeReservationType": "ANY_RESERVATION"
  },
  "hostname": "test.rherminizone.c.winter-form-254618.internal",
  "displayDevice": {
    "enableDisplay": false
  },
  "shieldedInstanceConfig": {
    "enableSecureBoot": false,
    "enableVtpm": true,
    "enableIntegrityMonitoring": true
  },
  "shieldedInstanceIntegrityPolicy": {
    "updateAutoLearnPolicy": true
  },
  "fingerprint": "5Qk_mOWY_Mk=",
  "kind": "compute#instance"
}

    print(get_Inst_Add())
    print(get_Inst_Info(data_to_parse)[2])





