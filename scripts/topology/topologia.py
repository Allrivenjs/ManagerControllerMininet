from mininet.topo import Topo

class MyTopology(Topo):
    def build(self):
        # Crea los switches
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
                    
        # Crea los hosts
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')
                    
        # Conecta los hosts a los switches
        self.addLink(host1, switch1)
        self.addLink(host2, switch2)
        self.addLink(host3, switch3)
                    
        # Conecta los switches en una topología en árbol
        self.addLink(switch1, switch2)
        self.addLink(switch2, switch3)
                    
topo = MyTopology()
