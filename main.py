from local_function import get_instance_info
from local_function import get_instance_ip

if __name__ == "__main__":
    data_to_parse = '{"insertId":"dljq86dn4km", "logName":"projects/winter-form-254618/logs/cloudaudit.googleapis.com%2Factivity","operation":{"id":"operation-1595403163215-5ab02bed1275e-413127fd-a7a69663","last":true,"producer":"compute.googleapis.com"}, "protoPayload":{"@type":"type.googleapis.com/google.cloud.audit.AuditLog", "authenticationInfo":{"principalEmail":"acheq.rhermini@gmail.com"},"methodName":"v1.compute.instances.start","request":{"@type":"type.googleapis.com/compute.instances.start"},"requestMetadata":{"callerIp":"176.176.74.253","callerSuppliedUserAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36,gzip(gfe),gzip(gfe)"},"resourceName":"projects/winter-form-254618/zones/us-central1-a/instances/instance-2","serviceName":"compute.googleapis.com"},"receiveTimestamp":"2020-07-22T07:32:55.17164028Z","resource":{"labels":{"instance_id":"1625421287170767075","project_id":"winter-form-254618","zone":"us-central1-a"},"type":"gce_instance"},"severity":"NOTICE","timestamp":"2020-07-22T07:32:54.44Z"}'
    print(get_instance_ip())
    print(get_instance_info(data_to_parse)[2])





