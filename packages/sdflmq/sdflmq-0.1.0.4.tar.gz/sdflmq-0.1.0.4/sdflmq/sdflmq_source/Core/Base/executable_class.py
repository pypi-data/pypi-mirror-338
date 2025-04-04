import paho.mqtt.client as mqtt
import time as T
import re
import os
from .topics import MQTTFC_Base
from random import randint
msg_size_limit = 10000000 #characters

#
#    client.start_loop() This starts the network loop on a background thread
#    client.loop_forever() This starts the network loop on the current thread and will block forever.
#    client.loop() this executes one cycle of the network loop and must be called as part of your own loop.

class PubSub_Base_Executable:

#EXECUTABLE PARAMS: 
        
        id = ""
        executables = ['print','echo_name','publish_executables'] #NOTE: Any method that wants to be controller executable, can be added to this list.
        introduction_topic = ''
        controller_executable_topic = ''
        controller_echo_topic = ''

#MQTT PARAMS:
        broker_ip = ''
        broker_port = 0000
        connection_timeout = 3600

#SECTION:: STARTUP
        def __init__(self,
                     myID,
                     broker_ip,
                     broker_port,
                     loop_forever = False):

            topics = MQTTFC_Base()

            self.is_connected = False
            self.id = myID
            self.broker_ip = broker_ip
            self.broker_port = broker_port
            self.introduction_topic = topics.introduction_topic
            self.controller_executable_topic = topics.controller_executable_topic
            self.controller_echo_topic = topics.controller_echo_topic

            self.msg_batch_queue = {} #{payload_id, [batch_id, msg_payload]}

            self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
            self.client.on_connect = self.on_connect
            self.client.on_message = self.msg_parse
            
            self.client.connect(self.broker_ip,
                                self.broker_port,
                                self.connection_timeout)
            
            
            self.root_directory =  os.getcwd() + "/" + self.id+"_data"
            if(os.path.isdir(self.root_directory) == False):
                os.mkdir(self.root_directory)

            print("Initiation Done.")

            self.loop_forever = loop_forever
            
            if(loop_forever):
                print("Starting base loop right away.")
                self.base_loop()
            else:
                while(self.is_connected == False):
                    print("waiting for connection")
                    self.oneshot_loop()
               

#SECTION:: CONNECTIVITY

        def msg_parse(self, client, userdata, msg):
            # try: 
                #print("MESSAGE: " + msg.payload.decode())
                header_body = str(msg.payload.decode()).split('::')
                # print("MESSAGE Header: " + header_body[0])
                header_parts = header_body[0].split('|')
                body = ""
                if(not(header_parts[2] in self.executables)):
                    self.ERROR_executable_not_defined(msg.payload.decode())
                    return
                if(header_parts[4] == "True"):
                    print("Received multi batch message. Batch " + str(header_parts[6]))
                    if(header_parts[6] != str(-1)):
                        if(header_parts[5] in self.msg_batch_queue):
                            self.msg_batch_queue[header_parts[5]].append([header_parts[6],header_body[1]])
                            # print(" batch index: " + str(self.msg_batch_queue[header_parts[5]][len(self.msg_batch_queue[header_parts[5]])-1][0]))
                        else:
                            self.msg_batch_queue[header_parts[5]] = [[header_parts[6],header_body[1]]]
                        return
                    else:
                        print("All batches received.")
                        body = self.MQTT_msg_merge(header_parts[5])
                else:
                    body = header_body[1]
                self.execute_on_msg(header_parts, body)
            # except Exception as e:  
                # print("Message was not right, or something wrong with one of the internal functions! See below:\n" + repr(e))


        def execute_on_msg (self, header_parts, body):                             ### TO OVERRIDE IN SUCCEEDING CLASSES            
            if header_parts[2] == 'print':
                body_split = body.split('-m ')[1].split(';')[0]
                self.print(body_split)

            if header_parts[2] == 'echo_name':
                self.echo_name()
            
            if header_parts[2] == 'echo_msg':
                self.echo_msg(body)
            
            if header_parts[2] == 'publish_executables':
                self.publish_executables()              
       
        def on_connect(self,client,userdata, flags, rc):
            print("Connected with result code " + str(rc))
            self.client.subscribe(self.controller_executable_topic,)
            self.is_connected = True
            print("Subscribed to " + self.controller_executable_topic)

        def MQTT_msg_craft(self,topic,func_name,msg,is_split = False, payload_id = '-1', batch_index = -1):
            payload = self.id + "|" + topic + "|" + func_name + "|" + T.asctime() + "|" + str(is_split) + "|" + payload_id + "|" + str(batch_index) +  "::" + str(msg)
            return payload
        
        def msg_sort_key(self,l):
            return int(l[0])
        
        def MQTT_msg_merge(self,payload_id):
            print("Merging batches.")
            
            #msg_batches = []
            # for batch in self.msg_batch_queue[payload_id]:
            #     msg_batches.append(batch)            
            # msg_batches.sort(key=self.msg_sort_key)

            self.msg_batch_queue[payload_id].sort(key=self.msg_sort_key)
            msg_payload = ""
            for batch in self.msg_batch_queue[payload_id]:
                msg_payload = msg_payload + batch[1]
            
            self.msg_batch_queue.pop(payload_id)
            print(len(self.msg_batch_queue))
            print("Batches merged.")
            print("payload size: " + str(len(msg_payload)))
            return msg_payload

        def MQTT_msg_split(self,msg,batch_size):
            payload_id = str(re.sub('[ :]','',str(T.asctime()))) + str(randint(0,1000000))
            msg_splits = []
            print("Splitting payload into " + str(int(len(msg)/batch_size)+1) + " batches.")
            print("payload size: " + str(len(msg)))
            print("Payload id is: " + payload_id)
            for j in range(0,len(msg),batch_size):
                i = int(j/batch_size)
                if((j)+batch_size >= len(msg)):
                    msg_splits.append([payload_id,i,msg[(j):len(msg)]])
                else:                  
                    msg_splits.append([payload_id,i,msg[(j):(j)+batch_size]]) #[payload_id, batch_id, msg_payload]
            return msg_splits

        def publish(self, topic, func_name, msg):
            is_split = False
            payload = ""
            if(len(msg)>msg_size_limit):
                is_split = True
                print("Message payload too large!")
                msg_batches = self.MQTT_msg_split(msg,msg_size_limit)
                for batch in msg_batches:
                    print("Publishing batch index " + str(batch[1]))
                    payload = self.MQTT_msg_craft(topic,func_name,batch[2],True,batch[0],batch[1])
                    self.client.publish(topic, payload = payload,qos=2)
                #End of batch::
                payload = self.MQTT_msg_craft(topic,func_name,"",True,batch[0],-1)
                self.client.publish(topic, payload = payload,qos=2)
            else:
                payload = self.MQTT_msg_craft(topic,func_name,msg)
                # print("publishing payload: " + payload)
                self.client.publish(topic, payload = payload,qos=2)
           
#SECTION:: EXECUTABLES
    
        def echo_name(self):
            print("Asking controller to echo my id:" + self.id)
            self.publish(topic=self.controller_echo_topic,func_name="echo_name",msg=self.id)

        def echo_msg(self,msg):
            print("Asking controller to echo my msg: " + msg)
            self.publish(topic=self.controller_echo_topic,func_name="echo_msg",msg=msg)

        def publish_executables(self):                                                                       ### TO OVERRIDE IN SUCCEEDING CLASSES
            msg = ''
            for item in self.executables:
                msg = msg + item + ","
            msg = msg[0:len(msg)-1]
            print("Publishing the list of executables ...")
            self.publish(self.introduction_topic,"publish_executables",msg)

        def print(self,msg):
            print(msg)

#SECTION:: EXECUTION EXCEPTIONS
        def ERROR_executable_not_defined(self,msg):
            print("Executable " + str(msg) + " is not defined.")
        
        def ERROR_executable_param_size_not_defined(self,msg):
            print("Executable " + str(msg) + " has undefined parameter size.")

#SECTION:: MAIN LOOP
        def base_loop(self):
            
            restore_count = 0 # Restoration Cap is 10
            while(True):
                error = ""
                try:
                    # print("Client loop forever started ...")
                    self.client.loop_forever()
                except OSError:
                    error = "Executable ran into error: " + OSError.strerror                                                                      
                    self.echo_msg(error)
                    if(restore_count < 10):
                        self.echo_msg("Client " + self.id + " is Restoring program...")
                        restore_count += 1
                        continue
                    else:
                        self.echo_msg("Client " + self.id + " maximum number of restoration reached. Killing instance. Recommending re-running the code.")
                        return -1
                    
        def oneshot_loop(self,callback = None,*args):
            
            restore_count = 0 # Restoration Cap is 10
            while(restore_count < 10):
                error = ""
                try:
                    # print("Client one-shot loop started ...")
                    self.client.loop()
                    if(callback != None):
                        callback(*args)
                    self.client.loop()
                    # print("Client one-shot loop ended ...")
                    return 0
                except OSError:
                    error = "Executable ran into error: " + OSError.strerror                                                                      
                    self.echo_msg(error)
                    self.echo_msg("Client " + self.id + " is Restoring program...")
                    restore_count += 1
                    continue
                   
            self.echo_msg("Client " + self.id + " maximum number of restoration reached. Killing instance. Recommending re-running the code.")
            return -1
        
        def parallel_loop(self):
            
            restore_count = 0 # Restoration Cap is 10
            while(restore_count < 10):
                error = ""
                try:
                    # print("Client parallel loop started on separate thread ...")
                    self.client.loop_start()
                    return 0
                except OSError:
                    error = "Executable ran into error: " + OSError.strerror                                                                      
                    self.echo_msg(error)
                    self.echo_msg("Client " + self.id + " is Restoring program...")
                    restore_count += 1
                    continue
            
            
            self.echo_msg("Client " + self.id + " maximum number of restoration reached. Killing instance. Recommending re-running the code.")
            return -1
        
        def end_parallel_loop(self):
            self.client.disconnect()
            print("Parallel loop ended. Thread terminated ...")
                        



