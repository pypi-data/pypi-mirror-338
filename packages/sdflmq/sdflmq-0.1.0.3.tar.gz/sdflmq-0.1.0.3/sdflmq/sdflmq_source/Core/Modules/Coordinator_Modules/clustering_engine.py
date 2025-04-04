from . import components as components
from .components import Cluster
from .components import Cluster_Node
from .components import Session

import math 

class Clustering_Engine():
    def __init__(self):
        return

    ###DESCRIPTION: A 2-layer topology is a tree-like topology in which the root node is the roo_aggregator, 
    # and level_1 leaves are aggregators or aggregator_trainers, and the level_2 leaves are trainer-only nodes. 
    # Example::
    ##                    [AGG____0]
    ##                   /     |     \
    ##              [AGG_1]   ...     [AGG_n]
    ##             /   |   \         /   |   \
    ##           [T1] [T2] [T3]  [Tk-2] [Tk-1] [Tk]
    ###_____________________________________________________________________________________________________
    ###_____________________________________________________________________________________________________
    
    def create_central_aggregation_topology(self,session): #TODO:incorporate 30,70 or 20,80 or ...
        if(len(session.client_list) < 4):
            print("Number of clients is not enough for a 2-layer hierarchical clustering.")
            return
        
        session.role_vector = []
        session.role_dictionary = {}
        num_aggregators = 1

        num_training_only = session.session_capacity_max - num_aggregators
        
        session.role_dictionary['agg_0'+ "_" + str(session.session_id)] = []
        session.role_vector.append(0)
        n_counter = 0
        for j in range(num_training_only):
            if(n_counter >= num_training_only):
                break
            else:
                session.role_dictionary['agg_0'+ "_" + str(session.session_id)].append('t_'+str(n_counter)+ "_" + str(session.session_id))     
                # session.role_dictionary['agg_' + str(i) + "_" + str(session.session_id)].append('t_'+str(n_counter)+ "_" + str(session.session_id))
                n_counter += 1
            

        return [session.role_vector,session.role_dictionary]

    def create_2layer_topology(self,session,percentage_of_aggs): #TODO:incorporate 30,70 or 20,80 or ...
        if(len(session.client_list) < 4):
            print("Number of clients is not enough for a 2-layer hierarchical clustering.")
            return
        
        session.role_vector = []
        session.role_dictionary = {}
        num_aggregators = math.floor(session.session_capacity_max * percentage_of_aggs)
        if(num_aggregators < 2):
            num_aggregators = 2

        num_training_only = session.session_capacity_max - num_aggregators
        num_trainer_per_l2_cluster = math.floor(num_training_only / (num_aggregators - 1))
        
        session.role_dictionary['agg_0'+ "_" + str(session.session_id)] = []
        session.role_vector.append(0)
        n_counter = 0
        for i in range(1,num_aggregators):
            session.role_dictionary['agg_0'+ "_" + str(session.session_id)].append('agg_' + str(i)+ "_" + str(session.session_id))
            session.role_vector.append(0)  
            session.role_dictionary['agg_' + str(i)+ "_" + str(session.session_id)] = []
            for j in range(num_trainer_per_l2_cluster):
                if(n_counter >= num_training_only):
                    break
                else:
                    session.role_dictionary['agg_' + str(i) + "_" + str(session.session_id)].append('t_'+str(n_counter)+ "_" + str(session.session_id))
                    n_counter += 1
            
        if(n_counter < num_training_only):#Distribute the remaining nodes to the aggregators, each receiving one of the remaining nodes
            for z in range(1,num_aggregators):
                if(n_counter >= num_training_only):
                    break
                else:
                    session.role_dictionary['agg_' + str(z) + "_" + str(session.session_id)].append('t_'+str(n_counter)+ "_" + str(session.session_id))
                    n_counter += 1

        return [session.role_vector,session.role_dictionary]
 
    def greedy_based_topology(self,session):
        #TODO: Read the calculated cost of FL in the previous round, and accordingly build a new role_vector, and feed it to the update_roles.
        session.update_roles([])
        return []

    def form_clusters(self,session):
        items = list(session.role_dictionary.keys())#check session.role_dictionary
        for i in range(len(items)):
            new_cluster = Cluster('cluster_' + str(i))

            new_node = None
            has_node = False
            for n in session.nodes:
                if(n.role == str(items[i])):
                    # print("already has node")
                    new_node = n
                    has_node = True
                    break
            if(has_node == False):
                new_node = Cluster_Node("N_" + str(len(session.nodes)),items[i],None) #First create the cluster head which has the role of aggregator
                new_node.status = components._NODE_PENDING
                session.nodes.append(new_node)#In each session, there is one root node which is the top-most aggregator. in role_dic it is 'agg_0'. If a given node is 'agg_0', then it is root node
            
            if(items[i] == "agg_0_" + str(session.session_id)):
                # new_node.role = components._ROLE_AGGREGATOR_ROOT
                session.set_root_node(new_node)
            
            new_cluster.set_cluster_head(new_node)
            
            for j in range(0,len(session.role_dictionary[items[i]])):#Now form clusters of nodes (not clients) based on the list of each aggregator's items
                new_sub_node = Cluster_Node("N_" + str(len(session.nodes)),session.role_dictionary[items[i]][j],None)
                new_sub_node.status = components._NODE_PENDING
                session.nodes.append(new_sub_node)
                # if(items[i][j][0] == 't'):
                #     new_sub_node.role = components._ROLE_TRAINER
                new_cluster.add_node(new_sub_node)
                
            session.add_cluster(new_cluster)
        #NOTE: All added nodes here are in pending mode. They will go to ACTIVE mode once the client they are assigned to, acknowledges the node's role.

        
        
        