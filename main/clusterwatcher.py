"""
Created on Jan 24, 2018

@author: Beatrice Moissinac

Usage: 
python3 clusterwatcher.py <AWS profile> <AWS Cluster Id> <Timer in minutes>
- <AWS profile>  is your aws cli configured profile
- <AWS Cluster Id> is the AWS cluster-id 
- <Timer in minutes> is the time in between each alert

Notes:
- The text/e-mail is sent from your own gmail address. You need to edit class Contact() with your sender/receiver information
- This script requires to have aws cli installed and configured with an AWS profile. 
- Script shut off automatically when cluster is not active
- Cannot send e-mails from OSU Gmails. For other traditional gmails, set your e-mail with "less secure apps"
https://support.google.com/accounts/answer/6010255
- To send a text message to your phone, find your carrier e-mails 
For instance T-mobile is PHONENUMBER@tmomail.net
Ref: https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/

Future Improvement:
- Manage several cluters
"""

import boto3
from time import sleep
import sys
import smtplib

def connectToAWS(profile):
    boto3.setup_default_session(profile_name=profile)  # Set profile
    client = boto3.client('emr')  # Client S3
    return client



def watch(client, clusterId, timer, contact):
    while True:
        print("Watcher on cluster "+clusterId)
        
        clusters = get_cluster_list(client)
        (active, status) = is_cluster_active(clusters, clusterId)
        
        if active:
            result = send_alert(contact, "Cluster "+clusterId+" is "+status)
            sleep(60 * timer)
        else:
            break
    pass


     
                    
        
def get_cluster_list(client):
    return client.list_clusters(ClusterStates=['STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING'])
        




# If cluster is active, return status
def is_cluster_active(clusters, clusterId):
    for cluster in clusters['Clusters']:         
        if cluster['Id'] == clusterId:
            return (True, cluster['Status']['State'])
    return (False, "Cluster is not active")
        
        
       

def send_alert(contact, message):
    header = 'From: %s\n' % contact.from_addr
    header += 'To: %s\n' % contact.to_addr
    header += 'Subject: Cluster Update\n\n' 
    message = header + message
    
    server = smtplib.SMTP(contact.smtpserver, 587)
    server.ehlo()
    server.starttls()
    server.login(contact.login, contact.password)
    problems = server.sendmail(contact.from_addr, contact.to_addr, message)
    server.close()
    return problems

        

class Contact():
    def __init__(self):
        self.smtpserver='smtp.gmail.com'
        self.from_addr = 'YOUR_EMAIL'
        self.to_addr   = 'EMAIL_OR_PHONE'
        self.login     = 'YOUR_EMAIL'
        self.password  = 'YOUR_PASSWORD'
        



if __name__ == '__main__':
    
    profile = sys.argv[1]
    clusterId = sys.argv[2]
    timer = int(sys.argv[3])
    
    contact = Contact() #Update with your contact info

    client = connectToAWS(profile)
    watch(client, clusterId, timer, contact)
    pass
