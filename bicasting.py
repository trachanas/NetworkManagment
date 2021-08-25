import os
import time
import matplotlib.pyplot as plt
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, OVSKernelAP
from mininet.link import TCLink
from mininet.log import setLogLevel, debug
from mininet.cli import CLI


import sys
gnet=None

car0_out_1 = 'car0_out_1.data'
client_out_1 = 'client_out_1.data'
ping_1 = 'ping_1.data'

car0_out_2 = 'car0_out_2.data'
client_out_2 = 'client_out_2.data'
ping_2 = 'ping_2.data'

"""car0_out_1 = 'car0_out_1.data'
car3_out_1 = 'car3_out_1.data'
car0_car3_ping_1 = 'car0_car3_ping_1.data'
car3_client_ping_1 = 'car3_client_ping_1.data'
car3_client_out = 'car3_client_out.data'
car3_out_c_1 = 'car3_out_c_1.data'
client_out_1 = 'client_out_1.data'
car3_out_s_1 = 'car3_out_s_1.data'


car0_out_2 = 'car0_out_2.data'
client_out_2 = 'client_out_2.data'
ping_2 = 'ping_2.data'

car0_out_3 = 'car0_out_3.data'
client_out_3 = 'client_out_3.data'
ping_3 = 'ping_3.data'
"""
# Implement the graphic function in order to demonstrate the network measurements
# Hint: You can save the measurement in an output file and then import it here
def graphic():
    
    #phase1
    f1 = open('car0_client.txt',"r")
    lines1 = f1.readlines()
    thr1 = []
    band1 = []
    jit1 = []
    pl1 = []
    for x in lines1:
        thr1.append(x.split(' ')[0])
    
    for x in lines1:
        band1.append(x.split(' ')[1])

    for x in lines1:
        jit1.append(x.split(' ')[2])

    for x in lines1:
        pl1.append(x.split(' ')[3])
    f1.close()

    f2 = open('ping_1.txt',"r")
    lines2 = f2.readlines()
    lat1 = []
    for x in lines3:
        lat1.append(x.split(' ')[0])
    f2.close()

    l1 = []
    l2 = []
    throughput = []
    bandwidth = []
    jitter = []
    p_lost = []
    latency = []

    for x in thr1:
        throughput.append(float(x))
    figure1 = plt.figure()
    figure1.suptitle('Throughput', fontsize = 35)
    plt.ylabel('KBps')
    plt.xlabel('Seconds')
    length = len(throughput)
    xlab = [i for i in range(1,length+1)]
    plt.xticks(xlab)
    plt.plot(throughput)
    figure1.savefig('bicasting_throughput_p1.jpeg')

    for x in jit1:
        jitter.append(float(x))
    figure2 = plt.figure()
    figure2.suptitle('Jitter', fontsize = 35)
    plt.ylabel('ms')
    plt.xlabel('Seconds')
    plt.xticks(xlab)
    plt.plot(jitter)
    figure2.savefig('bicasting_jitter_p1.jpeg')

    for x in lat1:
        latency.append(float(x))
    figure3 = plt.figure()
    figure3.suptitle('Latency', fontsize = 35)
    plt.ylabel('ms')
    plt.xlabel('Seconds')
    plt.xticks(xlab)
    plt.plot(latency)
    figure3.savefig('bicasting_latency_p1.jpeg')

    for x in pl1:
        temp = int(x.rpartition('/')[0])
        p_lost.append(temp)
    figure4 = plt.figure()
    figure4.suptitle('Packet Loss', fontsize = 35)
    plt.ylabel('Packets')
    plt.xlabel('Seconds')
    plt.xticks(xlab)
    plt.plot(p_lost)
    figure4.savefig('bicasting_packet_loss_p1.jpeg')

    #phase2
    del lines1[:]
    del thr1[:]
    del band1[:]
    del jit1[:]
    del pl1[:]
    del throughput[:]
    del bandwidth[:]
    del latency[:]
    del p_lost[:]
    del xlab[:]

    f1 = open('car0_client_phase2.txt',"r")
    lines1 = f1.readlines()
    for x in lines1:
        thr1.append(x.split(' ')[0])
    
    for x in lines1:
        band1.append(x.split(' ')[1])

    for x in lines1:
        jit1.append(x.split(' ')[2])

    for x in lines1:
        pl1.append(x.split(' ')[3])
    f1.close()


    f2 = open('car0_client_ping_phase2.txt',"r")
    lines2 = f2.readlines()
    lat1 = []
    for x in lines3:
        lat1.append(x.split(' ')[0])
    f2.close()

    for x in thr1:
        throughput.append(float(x))
    figure1 = plt.figure()
    figure1.suptitle('Throughput', fontsize = 35)
    plt.ylabel('KBps')
    plt.xlabel('Seconds')
    length = len(throughput)
    xlab = [i for i in range(1,length+1)]
    plt.xticks(xlab)
    plt.plot(throughput)
    figure1.savefig('bicasting_throughput_p2.jpeg')

    for x in jit1:
        jitter.append(float(x))
    figure2 = plt.figure()
    figure2.suptitle('Jitter', fontsize = 35)
    plt.ylabel('ms')
    plt.xlabel('Seconds')
    plt.xticks(xlab)
    plt.plot(jitter)
    figure2.savefig('bicasting_jitter_p2.jpeg')

    for x in lat1:
        latency.append(float(x))
    figure3 = plt.figure()
    figure3.suptitle('Latency', fontsize = 35)
    plt.ylabel('ms')
    plt.xlabel('Seconds')
    plt.xticks(xlab)
    plt.plot(latency)
    figure3.savefig('bicasting_latency_p2.jpeg')

    for x in pl1:
        temp = int(x.rpartition('/')[0])
        p_lost.append(temp)
    figure4 = plt.figure()
    figure4.suptitle('Packet Loss', fontsize = 35)
    plt.ylabel('Packets')
    plt.xlabel('Seconds')
    plt.xticks(xlab)
    plt.plot(p_lost)
    figure4.savefig('bicasting_packet_loss_p2.jpeg')




def apply_experiment(car,client,switch):
    x = 10
    time.sleep(2)
    print "Applying first phase"

    #mod flow rules
    os.system('ovs-ofctl mod-flows switch in_port=1,actions=drop')
    os.system('ovs-ofctl mod-flows switch in_port=2,actions=output:4')
    os.system('ovs-ofctl mod-flows switch in_port=4,actions=output:2,3')
    os.system('ovs-ofctl mod-flows switch in_port=3,actions=output:4')
    os.system('ovs-ofctl del-flows eNodeB1')
    os.system('ovs-ofctl del-flows eNodeB2')
    os.system('ovs-ofctl del-flows rsu1')
    
    car[0].cmd('ip route add 200.0.10.2 via 200.0.10.100')  #client is connected with enodeb2
    car[0].cmd('ip route del 200.0.10.2 via 200.0.10.50')
    client.cmd('ip route del 200.0.10.100 via 200.0.10.150')
    
    client.cmd('iperf -s -u -i 1 >> %s &' %client_out_1)
    time.sleep(2)
    car[0].cmd('ping 200.0.10.2 -c %d >> %s &' % (x,ping_1))
    car[0].cmd('iperf -c 200.0.10.2 -u -i 1 -t %d >> %s' % (x,car0_out_1))
    time.sleep(1)
    car[0].cmd('grep -v  "datagrams received out-of-order" /home/mininet/workspace/network_management/client_out_1.data | head -16 | tail -9 | tr  -s "  " | cut -d " " -f 6,8,10,12-13 > car0_client.txt')
    car[0].cmd('grep  -v "datagrams received out-of-order" /home/mininet/workspace/network_management/client_out_1.data | head -17 | tail -1 | tr -s "  " | cut -d " " -f 7,9,11,13-14 >> car0_client.txt')
    car[0].cmd('grep -v "DUP" /home/mininet/workspace/network_management/ping_1.data > ping_1_temp')
    car[0].cmd('tail -14 /home/mininet/workspace/network_management/ping_1_temp | head -10 | cut -d "=" -f 4 > ping_1.txt')
    os.remove("/home/mininet/workspace/network_management/ping_1_temp")

    
    CLI(gnet)
    print "Moving nodes"
    car[0].moveNodeTo('190,100,0')
    
    print "Applying second phase"
    os.system('ovs-ofctl mod-flows switch in_port=1,actions=drop')
    os.system('ovs-ofctl mod-flows switch in_port=3,actions=drop')
    os.system('ovs-ofctl mod-flows switch in_port=2,actions=output:4')
    os.system('ovs-ofctl mod-flows switch in_port=4,actions=output:2')
    os.system('ovs-ofctl del-flows eNodeB1')
    os.system('ovs-ofctl del-flows eNodeB2')
    os.system('ovs-ofctl del-flows rsu1')


    client.cmd('iperf -s -u -i 1 >> %s &' % client_out_2)
    time.sleep(2)
    car[0].cmd('ping 200.0.10.2 -c %d >> %s &' % (x,ping_2))
    car[0].cmd('iperf -c 200.0.10.2 -u -i 1 -t %d >> %s' % (x,car0_out_2))
    time.sleep(1)
    car[0].cmd('grep -v  "datagrams received out-of-order" /home/mininet/workspace/network_management/client_out_2.data | head -16 | tail -9 | tr  -s "  " | cut -d " " -f  6,8,10,12-13 > car0_client_phase2.txt')
    car[0].cmd('grep  -v "datagrams received out-of-order" /home/mininet/workspace/network_management/client_out_2.data | head -17 | tail -1 | tr -s "  " | cut -d " " -f 7,9,11,13-14 >> car0_client_phase2.txt')
    car[0].cmd('grep -v "DUP" /home/mininet/workspace/network_management/ping_3.data > ping_3_temp')
    car[0].cmd('tail -14 /home/mininet/workspace/network_management/ping_3_temp | head -10 | cut -d "=" -f 4 > ping_3.txt')
    os.remove("/home/mininet/workspace/network_management/ping_3_temp")



def topology():
    "Create a network."
    net = Mininet(controller=Controller, link=TCLink, switch=OVSKernelSwitch, accessPoint=OVSKernelAP)
    global gnet
    gnet = net
    
    print "*** Creating nodes"
    car = []
    stas = []
    for x in range(0, 4):
        car.append(x)
        stas.append(x)
    for x in range(0, 4):
        car[x] = net.addCar('car%s' % (x), wlans=2, ip='10.0.0.%s/8' % (x + 1), \
                            mac='00:00:00:00:00:0%s' % x, mode='b')


    eNodeB1 = net.addAccessPoint('eNodeB1', ssid='eNodeB1', dpid='1000000000000000', mode='ac', channel='1', position='80,75,0', range=60)
    eNodeB2 = net.addAccessPoint('eNodeB2', ssid='eNodeB2', dpid='2000000000000000', mode='ac', channel='6', position='180,75,0', range=70)
    rsu1 = net.addAccessPoint('rsu1', ssid='rsu1', dpid='3000000000000000', mode='g', channel='11', position='140,120,0', range=65)
    c1 = net.addController('c1', controller=Controller)
    client = net.addHost ('client')
    switch = net.addSwitch ('switch', dpid='4000000000000000')
    
    net.plotNode(client, position='125,230,0')
    net.plotNode(switch, position='125,200,0')
    
    print "*** Configuring wifi nodes"
    net.configureWifiNodes()
    
    print "*** Creating links"
    net.addLink(eNodeB1, switch)
    net.addLink(eNodeB2, switch)
    net.addLink(rsu1, switch)
    net.addLink(switch, client)
    
    print "*** Starting network"
    net.build()
    c1.start()
    eNodeB1.start([c1])
    eNodeB2.start([c1])
    rsu1.start([c1])
    switch.start([c1])
    
    for sw in net.vehicles:
        sw.start([c1])
    
    i = 1
    j = 2
    for c in car:
        c.cmd('ifconfig %s-wlan0 192.168.0.%s/24 up' % (c, i))
        c.cmd('ifconfig %s-eth0 192.168.1.%s/24 up' % (c, i))
        c.cmd('ip route add 10.0.0.0/8 via 192.168.1.%s' % j)
        i += 2
        j += 2
    
    i = 1
    j = 2
    for v in net.vehiclesSTA:
        v.cmd('ifconfig %s-eth0 192.168.1.%s/24 up' % (v, j))
        v.cmd('ifconfig %s-mp0 10.0.0.%s/24 up' % (v, i))
        v.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
        i += 1
        j += 2
    
    for v1 in net.vehiclesSTA:
        i = 1
        j = 1
        for v2 in net.vehiclesSTA:
            if v1 != v2:
                v1.cmd('route add -host 192.168.1.%s gw 10.0.0.%s' % (j, i))
            i += 1
            j += 2

    client.cmd('ifconfig client-eth0 200.0.10.2')
    net.vehiclesSTA[0].cmd('ifconfig car0STA-eth0 200.0.10.50')
    
    car[0].cmd('modprobe bonding mode=3')
    car[0].cmd('ip link add bond0 type bond')
    car[0].cmd('ip link set bond0 address 02:01:02:03:04:08')
    car[0].cmd('ip link set car0-eth0 down')
    car[0].cmd('ip link set car0-eth0 address 00:00:00:00:00:11')
    car[0].cmd('ip link set car0-eth0 master bond0')
    car[0].cmd('ip link set car0-wlan0 down')
    car[0].cmd('ip link set car0-wlan0 address 00:00:00:00:00:15')
    car[0].cmd('ip link set car0-wlan0 master bond0')
    car[0].cmd('ip link set car0-wlan1 down')
    car[0].cmd('ip link set car0-wlan1 address 00:00:00:00:00:13')
    car[0].cmd('ip link set car0-wlan1 master bond0')
    car[0].cmd('ip addr add 200.0.10.100/24 dev bond0')
    car[0].cmd('ip link set bond0 up')
   
    net.plotGraph(max_x=250, max_y=250)
    
    net.startGraph()
    
    # Uncomment and modify the two commands below to stream video using VLC
    car[0].cmdPrint("sudo vlc -vvv bunnyMob.mp4 --sout '#duplicate{dst=rtp{dst=200.0.10.2,port=5004,mux=ts},dst=display}' :sout-keep &")
    client.cmdPrint("sudo vlc rtp://@200.0.10.2:5004 &")
    
    car[0].moveNodeTo('95,100,0')
   
    
    os.system('ovs-ofctl del-flows switch') 
    time.sleep(3)
    
    apply_experiment(car,client,switch)
    
    # Uncomment the line below to generate the graph that you implemented
    graphic()
    
    # kills all the xterms that have been opened
    os.system('pkill xterm')
    
    print "*** Running CLI"
    CLI(net)
    
    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    try:
        topology()
    except:
        type = sys.exc_info()[0]
        error = sys.exc_info()[1]
        traceback = sys.exc_info()[2]
        print ("Type: %s" % type)
        print ("Error: %s" % error)
        print ("Traceback: %s" % traceback)
        if gnet != None:
            gnet.stop()
        else:
            print "No network"