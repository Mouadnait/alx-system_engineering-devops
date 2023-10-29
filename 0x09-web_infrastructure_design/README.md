# Alx School - 0x09-web_infrastructure_design
Whiteboarding tests for design of web application infrastructures

## Key concepts
* Network basics
* Server
* Web server
* Application server
* DNS & DNS record types
* Load Balancer
* Monitoring
* Database
* Single point of failure
* HTTP & HTTPS
* Firewall

## Helpful Links
### DNS
* [How does DNS work Webcomic](https://howdns.works/ep1/)
* [DNS record types](https://pressable.com/blog/2014/12/23/dns-record-types-explained/)
* [About /etc/hosts](http://www.linfo.org/etc_hosts.html)
* [Gandi.net Glue Records](https://wiki.gandi.net/en/glossary/glue-record)
* [SSL / TLS] (https://www.digicert.com/ssl.htm)
* [Round robin DNS](https://en.wikipedia.org/wiki/Round-robin_DNS)

### Errors
* [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
* [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)

### MySQL
* [Setup Master-Slave MySQL DBs](https://www.digitalocean.com/community/tutorials/how-to-set-up-master-slave-replication-in-mysql)

### Networks
* [Wikipedia: Autonomous System](https://en.wikipedia.org/wiki/Autonomous_system_(Internet))
* [Subdomains, Stackoverflow](https://serverfault.com/questions/275982/what-type-of-dns-record-is-needed-to-make-a-subdomain)

### Server network configuration
* [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
* [Load-balancing algorithms](https://devcentral.f5.com/articles/intro-to-load-balancing-for-developers-ndash-the-algorithms)
* [Round Robin DNS](https://www.dnsknowledge.com/whatis/round-robin-dns/)

### Servers
* [Application Server vs Web Server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [Wikipedia WSGI Servers Python](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface)
* [Wikipedia LAMP stack](https://en.wikipedia.org/wiki/LAMP_(software_bundle))

## Files

| Filename | Description |
| -------- | ----------- |
| `0-simple_web_stack` | Web Infrastructure Design with a LAMP stack. This contains: 1 server, 1 web server, 1 application server, 1 database and 1 domain name. |
| `1-distributed_web_infrastructure` | Web Infrastructure Design, based on `0-simple_web_stack` that contains some additional components: 1 server, 1 web server, 1 application server, 1 load-balancer, 1 set of application files, 1 database. |
| `2-secured_and_monitored_web_infrastructure` | Web Infrastructure Design, based on `1-distributed_web_infrastructure` that contains some additional components: 3 firewalls, 1 SSL certificate, 3 monitoring clients. |
| `3-scale_up` | Web Infrastructure Design, based on `2-secured_and_monitored_web_infrastructure` that contains some additional components: 1 server, 1 load-balancer. |
