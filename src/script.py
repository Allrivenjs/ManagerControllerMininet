from mininet.topo import Topo

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

    def __init__( self ):
        # Initialize topology
        Topo.__init__( self )

        hosts = self.setup_hosts()
        switches = self.setup_switches()

        connection_tree = {}

        for switch in switches:
            switches_copy = switches.copy()
            switches_copy.remove(switch)

            print("Switches disponibles")
            print(switches_copy)

            print("Hosts disponibles")
            print(hosts)

            element_to_connect = input(f"Con que elemento desea conectar el switch {switch}:>_ ")

            if element_to_connect in switches or element_to_connect in hosts:
                self.connect_elemets(switch, element_to_connect, connection_tree)
            else:
                print("Elemento desconocido")

        for host in hosts:
            hosts_copy = hosts.copy()
            hosts_copy.remove(host)

            print("Switches disponibles")
            print(switches)

            print("Hosts disponibles")
            print(hosts_copy)

            element_to_connect = input(f"Con que elemento desea conectar el host {host}:>_ ")

            if element_to_connect in switches or element_to_connect in hosts:
                self.connect_elemets(host, element_to_connect, connection_tree)
            else:
                print("Elemento desconocido")

        print(connection_tree)

        self.create_links(connection_tree)


topos = { 'mytopo': ( lambda: MyTopo() ) } 

 
