1. Cài đặt docker
Xem ở file install_docker.md
2. Cài đặt ELK Stack
```bash
git clone https://github.com/thangphan205/docker-elk.git
cd docker-elk
docker compose up setup
docker compose up -d
```

3. Truy cập ELK giao diện
```bash
http://<IP_SERVER>:5601
Username: elastic
Default Password: changeme_UCzc1Twlw3qGIuCJ4Mai
```

4. Thêm quyền cho role logstash_writer
Khi bạn thấy log xuất hiện tương tự như vậy thì thêm quyền auto_configure cho role logstash_writer
```bash
[2026-01-01T15:48:05,321][INFO ][logstash.outputs.elasticsearch][main][8a66b2d49f621ff56731d24e7f0ff98e27149d52838489ad78e4131783c42619] Retrying failed action {:status=>403, :action=>["index", {:_id=>nil, :_index=>"network-juniper-2026.01", :routing=>nil}, {"service"=>{"type"=>"system"}, "message"=>"audit: type=1400 audit(1767282230.922:14667272): apparmor=\"DENIED\" operation=\"mknod\" class=\"file\" profile=\"rsyslogd\" name=\"/run/syslogd.pid.tmp\" pid=1270761 comm=\"rsyslogd\" requested_mask=\"c\" denied_mask=\"c\" fsuid=0 ouid=0", "log"=>{"syslog"=>{"facility"=>{"code"=>0, "name"=>"kernel"}, "severity"=>{"code"=>5, "name"=>"Notice"}, "priority"=>5}}, "process"=>{"name"=>"Kernel"}, "@version"=>"1", "@timestamp"=>2026-01-01T22:36:00.000Z, "tags"=>["juniper_network"], "event"=>{"original"=>"<5>Jan  1 22:36:00 juniper1 Kernel: audit: type=1400 audit(1767282230.922:14667272): apparmor=\"DENIED\" operation=\"mknod\" class=\"file\" profile=\"rsyslogd\" name=\"/run/syslogd.pid.tmp\" pid=1270761 comm=\"rsyslogd\" requested_mask=\"c\" denied_mask=\"c\" fsuid=0 ouid=0"}, "type"=>"juniper", "host"=>{"ip"=>"172.25.245.232", "hostname"=>"juniper1"}}], :error=>{"type"=>"security_exception", "reason"=>"action [indices:admin/auto_create] is unauthorized for user [logstash_internal] with effective roles [logstash_writer] on indices [network-juniper-2026.01], this action is granted by the index privileges [auto_configure,create_index,manage,all]"}}
```

.... 4.1. Vào Stack Management > Roles.

.... 4.2. Tìm role logstash_writer.

.... 4.3. Trong phần Index privileges, tìm index pattern tương ứng (hoặc thêm network-*).

.... 4.4.Thêm quyền auto_configure và create_index (hoặc chọn all để đơn giản hóa).

.... 4.5. Nhấn Save.

5. Alerts
