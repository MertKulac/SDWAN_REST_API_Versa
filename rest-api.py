[appadmin@mert ~]$ curl -v -k -u SDWAN-DASHBOARD:HAJtv678 "https://160.159.228.51:9182/api/config/system" -H "Accept:application/json" -H "Content-Type:application/json"
* About to connect() to 160.159.228.51 port 9182 (#0)
*   Trying 160.159.228.51...
* Connected to 160.159.228.51 (160.159.228.51) port 9182 (#0)
* Initializing NSS with certpath: sql:/etc/pki/nssdb
* skipping SSL peer certificate verification
* SSL connection using TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
* Server certificate:
*       subject: CN=CUSTOMER-A-Director-01,OU=VersaDirector,O=versa-networks,ST=California,C=US
*       start date: Jul 04 21:11:09 2022 GMT
*       expire date: Oct 06 21:11:09 2024 GMT
*       common name: CUSTOMER-A-Director-01
*       issuer: L=Santa Clara,ST=California,C=US,OU=VersaDirector,O=versa-networks,CN=CUSTOMER-A-Director-01
* Server auth using Basic with user 'SDWAN-DASHBOARD'
> GET /api/config/system HTTP/1.1
> Authorization: Basic U0RXQU4tREFTSEJPQVJEOkhBSnR2Njc4
> User-Agent: curl/7.29.0
> Host: 160.159.228.51:9182
> Accept:application/json
> Content-Type:application/json
> 
< HTTP/1.1 200 
< accept: application/vnd.yang.data+json
< Accept-Encoding: deflate
< Etag: "1660-44577-592755@160.159.228.51"
< Last-Modified: Wed, 22 Jun 2022 18:50:36 GMT
< Response-CUSTOMER-Ae: Tue, 09 Aug 2022 14:29:40 TRT
< Server: VersaDirector
< url: /config/system
< X-Content-Type-Options: nosniff
< X-XSS-Protection: 1; mode=block
< Cache-Control: no-cache, no-store, max-age=0, must-revalidate
< Pragma: no-cache
< Expires: 0
< Strict-Transport-Security: max-age=31536000 ; includeSubDomains
< X-Frame-Options: DENY
< Content-Type: application/vnd.yang.data+json
< Content-Length: 685
< Date: Tue, 09 Aug 2022 11:29:40 GMT
< 
{
  "system" : {
    "settings" : {
      "encrypt-data" : {
        "enable-encrypting-sensitive-info" : false
      }
    },
    "dns" : { },
    "ntp" : {
      "server" : [ {
        "name" : "160.154.215.21"
      }, {
        "name" : "160.154.216.40"
      }, {
        "name" : "160.154.216.41"
      }, {
        "name" : "160.2160.19.34"
      } ]
    },
    "address" : {
      "south-bound" : {
        "ip-address-list" : [ {
          "ip-address" : "160.159.228.116"
        } ]
      }
    },
    "CUSTOMER-Ae-zone" : "Europe/Istanbul",
    "syslog-servers" : {
      "server" : [ {
        "host" : "160.102.111.110"
      }, {
        "host" : "160.218.166.87"
      } ]
    }
  }
* Connection #0 to host 160.159.228.51 left intact

