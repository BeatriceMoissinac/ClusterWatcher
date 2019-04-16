# ClusterWatcher
A watcher for AWS EMR clusters, because I forgot to turn them off too many times...

## Usage: 
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