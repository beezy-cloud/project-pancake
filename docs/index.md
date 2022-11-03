# Project Pancake 

Project Pancake is a codename for demonstrating the concept of semi-autonomous edge devices being handled by micro-services running on Kubernetes.  
This is the perfect illustration of the Open Hybrid Cloud. 


```mermaid 
    C4Context
      title Project Pancake
      Enterprise_Boundary(b0, "") {
        Person(Pilot, "RHSC Pilot")

        Enterprise_Boundary(b3, "Private Cloud"){
          System(ControlStation, "Control Station")
          System(ControlService, "Control Service")
        }

        Enterprise_Boundary(b6, "Networking"){
          System(PubNetwork, "Public Network Infrastructure")
          System(PrvNetwork, "Private Mobile Network")
        }

        Enterprise_Boundary(b2, "Public Cloud") {
          Enterprise_Boundary(c1, "OpenShift"){
            System(MongoDB, "MongoDB")
            System(Prometheus, "Prometheus")
            System(Grafana, "Grafana")
            System(Website, "Website")
          }
        }

        Enterprise_Boundary(b4, "Edge Gateway"){
          System(EdgeGateway, "Edge Device")
        }
        Enterprise_Boundary(b5, "Edge"){
          System(EdgeDevice, "Edge Device")
        }

        Person(Supervisor, "RHSC Supervisor")
        Person(Public, "World Citizen")
      }


      Rel(Personal, ControlStation, "Generate a payload")

      Rel(ControlStation, PubNetwork, "Payload on Transit")
      Rel(PubNetwork, ControlService, "")
      
      Rel(ControlStation, PrvNetwork, "Payload on Transit")
      Rel(PrvNetwork, ControlService, "")
      
      Rel(ControlService, Prometheus, "")
      Rel(Grafana, Prometheus, "")
      Rel(ControlService, EdgeGateway, "Relay payload")
      Rel(EdgeGateway, EdgeDevice, "Execute payload and send back payload")

      Rel(Public, Website, "")
      Rel(Personal, Grafana, "")

      UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="1")
```

<!-- 
      UpdateElementStyle(customerA, $fontColor="red", $bgColor="grey", $borderColor="red")
      UpdateRelStyle(customerA, SystemAA, $textColor="blue", $lineColor="blue", $offsetX="5")
      UpdateRelStyle(SystemAA, SystemE, $textColor="blue", $lineColor="blue", $offsetY="-10")
      UpdateRelStyle(SystemAA, SystemC, $textColor="blue", $lineColor="blue", $offsetY="-40", $offsetX="-50")
      UpdateRelStyle(SystemC, customerA, $textColor="red", $lineColor="red", $offsetX="-50", $offsetY="20")

      UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="2") -->