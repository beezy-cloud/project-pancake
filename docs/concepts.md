
The below concept definitions are based on field user experience and not from an academic standpoint. The latter will have a foot note reference.  

## Edge[^1]
Depending of the industry and core business, the definition of Edge computing might be totally different.  
From a generic standpoint, edge computing is a device outside of the main computing premise of an organization ranging from a branch office to a water level sensor.  

Here are some generic use cases:
- for retails like a Target, the Point of Sales (PoS) where you checkout is an edge device or the Alexa devices for AWS.
- for banks like Bank of Scotland, the Automated Teller Machine (ATM) where you get cash from is an edge device or the payment device at a retail shop. 
- for telecom companies like NTT Docomo, a cell tower is an edge device or a smartphone is also a edge device.
- for Public Services like USGS, sensors in lakes and rivers are edge devices.
- for a media company like Amazon, a FireTV stcik is an edge device.

Within Project Pancake, our Edge device is a piece of equipment hundred miles away from the main computing premise and connected to a untrusted network.  
Considering this scenario, an Edge gateway might be used to repeat the data path from a down- and upstream perspective to avoid data lost. 

## Container[^2]
The term container is used to define a way to package an application with the necessary libraries for this application to run.  
That packaging is supposed to run seamlessly on any container platforms regardless of its composition as long as the packaging is respectfull of the open standards ([OCI](https://opencontainers.org/about/overview/)).  
In other words, there is not need anymore to perform deep compatibility analysis to ensure an application can run a specific version of Linux with libraries and hardware.  
On top of this, since the container will include the necessary libraries for the application to run, any patching or upgrade at the lower level, aka the Operating System, will not impact the application.  

## Microservice[^3]

## Kubernetes[^4]

## GitOps[^5]





[^1]: [Edge device](https://en.wikipedia.org/wiki/Edge_device)   
[^2]: [Containerization](https://en.wikipedia.org/wiki/Containerization_(computing))   
[^3]: [Microservices](https://en.wikipedia.org/wiki/Microservices)  
[^4]: [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes)  
[^5]: [GitOps](https://en.wikipedia.org/wiki/DevOps#GitOps)  