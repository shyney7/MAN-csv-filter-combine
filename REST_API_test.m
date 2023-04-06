% pt = posixtime(datetime('now', 'TimeZone', 'local'))
pt = convertTo(datetime('now', 'TimeZone', 'local'), 'epochtime', 'TicksPerSecond', 1e9);
uri = matlab.net.URI('http://10.40.14.18:8086/api/v2/write?org=roboflex&bucket=roboflex-test1&precision=ns');
token = 'Token p0k3mq6iixbzG_PH_B-rWDNF3N9DfPrf03_QmoX53N7mCYAHHjFKxnawCwzWz6WY5xTnaJiHh-o-qp9Py7J-Aw==';

data = "testmeasurement,pseudotag=pseudo1 test_percent=";

pseudoValue = 46.77;

data = append(data, num2str(pseudoValue));
data = append(data, ' ');
data = append(data, num2str(pt));

body = matlab.net.http.MessageBody(data);

header = matlab.net.http.HeaderField('Authorization', token);

method = matlab.net.http.RequestMethod.POST;
request = matlab.net.http.RequestMessage(method, header, body);

response = send(request, uri);
if (response.Completed)
    fprintf("writing to influxdb successful")
end
