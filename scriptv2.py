from mininet.topo import Topo

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController

class MyTopo( Topo ): 

    def setup_switches(self):
        switches = []

        swiches_n = int(input("Cuantos swiches quiere?: >_ "))

        for i in range(swiches_n):
            new_switch = self.addSwitch( f's{i}' )
            switches.append(new_switch)

        return switches

    def setup_hosts(self):
        hosts = []

        host_n = int(input("Cuantos hosts quiere?: >_ "))

        for i in range(host_n):
            new_host = self.addHost( f'h{i}' )
            hosts.append(new_host)

        return hosts

    def connect_elemets(self, element1, element2, connection_tree):
        if connection_tree.get(element1) is not None:
            connection_tree[element1] = [*connection_tree[element1], element2]
        else:
            connection_tree[element1] = [element2]
        
    def create_links(self, connection_tree):
        connection_tree_keys = list(connection_tree.keys())

        for key in connection_tree_keys:
            for element in connection_tree[key]:
                self.addLink( key, element )

    def fill_switches(self, switches, hosts, connection_tree):
        for switch in switches:
            switches_copy = switches.copy()
            switches_copy.remove(switch)

            print("Switches disponibles")
            print(switches_copy)

            print("Hosts disponibles")
            print(hosts)

            input_string = input(f"Con que elementos desea conectar el switch {switch}:>_ ")
            elements_to_connect = input_string.split()

            for element in elements_to_connect:
                if element in switches or element in hosts:
                    self.connect_elemets(switch, element, connection_tree)
                else:
                    print("Elemento desconocido")

    def fill_hosts(self, switches, hosts, connection_tree):
        for host in hosts:
            hosts_copy = hosts.copy()
            hosts_copy.remove(host)

            print("Switches disponibles")
            print(switches)

            print("Hosts disponibles")
            print(hosts_copy)

            input_string = input(f"Con que elemento desea conectar el host {host}:>_ ")
            elements_to_connect = input_string.split()

            for element in elements_to_connect:
                if element in switches or element in hosts:
                    self.connect_elemets(host, element, connection_tree)
                else:
                    print("Elemento desconocido")
        

    def __init__( self ):
        # Initialize topology
        Topo.__init__( self )

        hosts = self.setup_hosts()
        switches = self.setup_switches()

        connection_tree = {}

        self.fill_switches(switches, hosts, connection_tree)
        self.fill_hosts(switches, hosts, connection_tree)

        print(connection_tree)

        self.create_links(connection_tree)



if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')

    ip_address = input("Ingrese la ip del controlador remoto:>_ ")
    port = input("Ingrese el puerto del controlador remoto:>_ ")

    topo = MyTopo()

    net = Mininet(topo=topo,

        controller=None,
        autoStaticArp=True)

    net.addController("c0",
        controller=RemoteController,
        ip=ip_address,
        port=int(port))

    net.start()
    CLI(net)
    net.stop() 
