from xml.etree import ElementTree
import libvirt
import time

conn = libvirt.open('qemu:///system')
data = {}
for i in conn.listDomainsID():
    dom = conn.lookupByID(i)
    data[dom.name()] = {}
    # cpu
    t1 = time.time()
    c1 = int(dom.info()[4])
    time.sleep(1)
    t2 = time.time()
    c2 = int(dom.info()[4])
    c_nums = int(dom.info()[3])
    usage = (c2 - c1) * 100 / ((t2 - t1) * c_nums * 1e9)
    # print dom.name(), "{0}%".format(usage)
    data[dom.name()]["cpu"] = "{0}%".format(usage)
    # memory
    meminfo = dom.memoryStats()
    free_mem = float(meminfo['unused'])
    total_mem = float(meminfo['available'])
    util_mem = ((total_mem - free_mem) / total_mem) * 100
    # print (str(domain.name()) + ' Memory usage :' + str(util_mem))
    data[dom.name()]["memory"] = "{0}%".format(util_mem)

    tree = ElementTree.fromstring(dom.XMLDesc())
    i_faces = tree.findall('devices/interface/target')
    for j in i_faces:
        iface = j.get('dev')
        # net
        ifaceinfo = dom.interfaceStats(iface)
        print dom.name(), iface, ifaceinfo
        read_1 = ifaceinfo[0]
        write_1 = ifaceinfo[4]
        time.sleep(1)
        ifaceinfo_2 = dom.interfaceStats(iface)
        read_2 = ifaceinfo_2[0]
        write_2 = ifaceinfo_2[4]

    tree = ElementTree.fromstring(dom.XMLDesc())
    devices = tree.findall('devices/disk/target')
    for d in devices:
        device = d.get('dev')
        devstats = dom.blockStats(device)
        print dom.name(), device, devstats
        rd_bytes = devstats[1]
        wr_bytes = devstats[3]
