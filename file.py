#!/usr/bin/env python

f = file("keepalived-lvs01.conf")
t = file("test.txt","r+")
h = """! Configuration File for keepalived

global_defs {
   router_id LVS_G1_02
}

vrrp_sync_group VGKU {
   group {
      VI_READ_KU
   }
}


vrrp_instance VI_READ_KU {
    state BACKUP
    interface bond0.192
    virtual_router_id 40
    priority 90
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass lvs01
    }
"""
for i in f.readlines()[21:]:
    t.write( i )

t = file("test.txt","r")
content = t.read()
pos = content.find("    virtual_ipaddress")
#pos等于0的时候表示能find到。
if pos != -1:
    content = content[:pos] + h +content[pos:]
    t = file("test.txt","w")
    t.write( content )
    print "ok"
