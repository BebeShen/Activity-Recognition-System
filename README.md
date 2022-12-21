# Activity-Recognition-System

IOT Final Project : Activity-Recognition-System

- [x]  Device Application ( See [Section 1](https://github.com/BebeShen/Activity-Recognition-System/edit/main/README.md#device-application) )
    - [x]  Sensor
    - [x]  simulation environment
- [x]  om2m Architecture, MN-CSE to IN-CSE to Server ( See [Section 2](https://github.com/BebeShen/Activity-Recognition-System/edit/main/README.md#om2m-Architecture) )
    - [x]  Connect MN-CSE &  IN-CSE
    - [x]  Subscribe to DATA container
- [x]  Collect Data & Activity Recognition ( See [Section 3](https://github.com/BebeShen/Activity-Recognition-System/edit/main/README.md#Activity-Recognition) )
    - [x]  python server
    - [x]  GUI (?)
    
## Device Application
* 妤婷
1. Define the simulation environment & situation
2. Define all DA ( USE App inventor or node-red inject node )
3. **After DA definition, please tell what data are delievered**

### DA

- BedWeight -> Boolean
- Light -> Boolean
- Broom -> Boolean
- Mop -> Boolean
- Temp -> int: 10~30
- AirCon -> Boolean
- Motion -> Boolean
- Door -> Boolean

## om2m Architecture
* 子揚
1. Connect all CSEs
2. Subscribe to DATA containers
3. Post to server (node-red)

## Activity Recognition
* 以新
1. Collect Data
2. Activity Recognition
3. Presentation

## Usage

### Step 1: start 1 in-cse & 2 mn-cse

```txt
# content of mn-cse1/configuration/config.ini

org.eclipse.equinox.http.jetty.http.port=8282
org.eclipse.om2m.cseBaseContext=/
org.eclipse.om2m.cseBaseProtocol.default=http
org.eclipse.om2m.cseBaseName=mn-name
org.eclipse.om2m.cseBaseAddress=127.0.0.1
org.eclipse.om2m.cseBaseId=mn-cse
```

```
# content of mn-cse2/configuration/config.ini

org.eclipse.equinox.http.jetty.http.port=8383
org.eclipse.om2m.cseBaseContext=/
org.eclipse.om2m.cseBaseProtocol.default=http
org.eclipse.om2m.cseBaseName=mn-name2
org.eclipse.om2m.cseBaseAddress=127.0.0.1
org.eclipse.om2m.cseBaseId=mn-cse2
```

So, `mn-cse1` is http://127.0.0.1:8282/webpage and `mn-cse2` is http://127.0.0.1:8383/webpage, and if 3 cse start gracefully, you would see the correct in-cse resource tree like following:

![](/images/in-cse.png)

### Step 2: start node-red & import flows

In terminal:
```shell
node-red
```

Then, open http://127.0.0.1:1880/ , and import `mn-cse.json` & `in-cse.json`

![](/images/importFlows.png)

Click `Deploy` to restart node-red flow

### Step 3: start http server

Install prerequisite module:

```shell
pip install fastapi uvicorn
sudo apt-get install python3.10-tk
```

Start server: 

```shell
uvicorn main:app --reload
# or
uvicorn main:app --reload --log-level "error"
```

Then you should see the server running on `8000` port

### Step 4: Create Application & Container & Do Subscription

![](/images/node-red_mn-cse.png)
![](/images/node-red_in-cse.png)

1. Create IN-CSE Application
2. Create IN-CSE Container
3. Subscribe to IN-CSE Data Container (this will parse data well and send request to  server)
4. Create MN-CSE Application
5. Create MN-CSE Container
6. Subscribe to MN-CSE Data Container (this will duplicate contentInstance to IN-CSE)

After the operations below, you could click `ContentInstance` in `MN-CSE` to change sensor data. 
Then inject the node.

![](/images/result.png)

## Reference

* [Evidential fusion of sensor data for activity recognition in smart homes](https://www.sciencedirect.com/science/article/abs/pii/S157411920800045X)
* [Multiple gateways scenario reference](https://wiki.eclipse.org/OM2M/one/Starting#Multiple_gateways_scenario)
