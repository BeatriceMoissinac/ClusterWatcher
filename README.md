# ClusterWatcher
A watcher for AWS EMR clusters, because I forgot to turn them off too many times...

## Usage 
`python3.6 clusterwatcher.py <AWS profile> <AWS Cluster Id> <Timer in minutes>`

Where:
* `<AWS profile>`  is your aws cli configured profile
* `<AWS Cluster Id>` is the AWS cluster-id (e.g., J-XX...XXX) 
* `<Timer in minutes>` is the amount of time in between each alert

## Setting e-mail/text
* The text/e-mail is sent from your own email address. You need to edit class Contact() with your sender/receiver information
* This script requires to have aws cli installed and configured with an AWS profile. 
* Script shut off automatically when cluster is not active
* Cannot send e-mails from OSU Gmails. For other traditional gmails, set your e-mail with "less secure apps"
https://support.google.com/accounts/answer/6010255
* To send a text message to your phone, find your carrier e-mails 
For instance T-mobile is PHONENUMBER@tmomail.net
Ref: https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/

## Future Improvement
Watch several cluters
