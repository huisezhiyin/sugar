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
    data[dom.name()]["cpu"] = "{0}%".format(usage)

    # memory
    meminfo = dom.memoryStats()
    free_mem = float(meminfo['unused'])
    total_mem = float(meminfo['available'])
    util_mem = ((total_mem - free_mem) / total_mem) * 100
    data[dom.name()]["memory"] = "{0}%".format(util_mem)

    tree = ElementTree.fromstring(dom.XMLDesc())
    # net
    for tmp_net in tree.findall('devices/interface/target'):
        dev = tmp_net.get('dev')
        network_info = dom.interfaceStats(dev)
        read_bytes1 = network_info[0]
        write_bytes1 = network_info[4]
        time.sleep(1)
        network_info = dom.interfaceStats(dev)
        read_bytes2 = network_info[0]
        write_bytes2 = network_info[4]
        write = write_bytes2 - write_bytes1
        read = read_bytes2 - read_bytes1


    # disk
    for tmp_disk in tree.findall('devices/disk/target'):
        dev = tmp_disk.get('dev')
        disk_info = dom.blockStats(dev)
        read_bytes1 = disk_info[1]
        write_bytes1 = disk_info[3]
        time.sleep(1)
        disk_info = dom.blockStats(dev)
        read_bytes2 = disk_info[1]
        write_bytes2 = disk_info[3]
        write = write_bytes2 - write_bytes1
        read = read_bytes2 - read_bytes1
