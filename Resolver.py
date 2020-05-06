import socket
import os
from scapy.all import ARP, Ether, srp

menu = 1
end = False

#Main Menu
while not end:
  if menu == 1:
    os.system('clear')
    print("Papa Snags Local IP / Hostname Resolver")
    print("1. Local IP Address scan")
    print("2. Hostname Resolver")
    print("3. About")
    print("4. Exit")
    sel = input("Please Select an option: ")
    if sel == '1':
        menu = 2
    if sel == '2':
      menu = 3
    if sel == '3':
        menu = 4
    if sel == '4':
        os.system('clear')
        exit()

#Local IP Address Scanner Menu
  if menu == 2:
    if not end:
        os.system('clear')
        print("SCANNING....")
        hostname = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
        if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
        s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
        socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

        target_ip = (hostname+"/24")
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    os.system('clear')
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))
    print("")
    print("1. Rescan")
    print("2. Go back")
    opt = input("Please Select an option: ")
    if opt == "1":
        menu = 2
    if opt == "2":
        menu = 1

#Hostname Resolver Menu
  if menu == 3:
    if not end:
        os.system('clear')
        ip = input("Enter IP Address: ")
        print ("Hostname: " + socket.getfqdn(ip))
        print("")
        print("1. Enter another IP")
        print("2. Go back")
        opt = input("Please Select an option: ")
        if opt == "1":
            menu = 3
        if opt == "2":
            menu = 1

#About menu
  if menu == 4:
    if not end:
        os.system('clear')
        print("Made by PapaSnags")
        print("Twitter: @PapaSnags")
        print("GitHub: @PapaSnags")
        print("Discord: Papa.Snags#1555")
        print("Website: papa-snags.com")
        print("")
        print("1. Go back")
        opt = input("Please Select an option: ")
        if opt == "1":
                menu = 1
