
The below concept definitions are based on field user experience and not from an academic standpoint. The latter will have a foot note reference.  

## Edge
Depending of the industry and core business, the concept of Edge computing might be totally different.  
From a generic standpoint, edge computing is a device outside of the main computing premise of an organization ranging from a branch office to a water level sensor.  

Here are some generic use cases:
- for retails like a Target, the Point of Sales (PoS) where you checkout is an edge device or the Alexa devices for AWS.
- for banks like Bank of Scotland, the Automated Teller Machine (ATM) where you get cash from is an edge device or the payment device at a retail shop. 
- for telecom companies like NTT Docomo, a cell tower is an edge device or a smartphone is also a edge device.
- for Public Services like USGS, sensors in lakes and rivers are edge devices.
- for a media company like Amazon, a FireTV stcik is an edge device.

Within Project Pancake, our Edge device is a piece of equipment hundred miles away from the main computing premise and connected to a untrusted network.  
Considering this scenario, an Edge gateway might be used to repeat the data path from a down- and upstream perspective to avoid data lost. 

[Edge device on Wikipedia](https://en.wikipedia.org/wiki/Edge_device)  

## Container
The concept of container is used to define a way to package an application with the necessary libraries for this application to run.  
That packaging is supposed to run seamlessly on any container platforms regardless of its composition as long as the packaging is respectfull of the open standards ([OCI](https://opencontainers.org/about/overview/)).  
In other words, there is not need anymore to perform deep compatibility analysis to ensure an application can run a specific version of Linux with libraries and hardware.  
On top of this, since the container will include the necessary libraries for the application to run, any patching or upgrade at the lower level, aka the Operating System, will not impact the application.  

[Containerization on Wikipedia](https://en.wikipedia.org/wiki/Containerization_(computing)) 

## Microservice
The concept of microservice is often associated with the containerization of applications. While an application could be composed of multiple modules composing a single unit, microservices would decouple these modules in multiple small servides.  
As an example, if an online retail company as an e-commerce, this application might pack as one single unit (also called monolith) the following modules: 
- front-end web module
- search module 
- suggestion module
- payment module
- shipping module
- caching module

Within the world of microservice and container, these modules would all have their own container, so 6 containers, instead of 1.  
This approach provides more flexibility from a development and lifecycle perspectice as patching or updating the code from one of the service would not impact the entire stack. 
Also, having the shipping module failing will not impact the entire shopping experience as the transactions will be reconciled later. 

[Microservices on Wikipedia](https://en.wikipedia.org/wiki/Microservices)  

## Kubernetes


[Kubernetes on Wikipedia](https://en.wikipedia.org/wiki/Kubernetes)  

## GitOps

 
[GitOps on Wikipedia](https://en.wikipedia.org/wiki/DevOps#GitOps)  