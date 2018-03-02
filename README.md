# S3 Automated ACL Remediation

## CloudFormation
This template will deploy an AWS Lambda function that will respond to CloudTrail Events for S3 bucket creation.
#### Ohio region only
### Installation Guide
1. <a href="https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=S3-AutoLock&templateURL=https://s3.amazonaws.com/infascination-public-oregon/cfn-templates/s3-autolock.template" target="_blank">![Launch](./img/launch-stack.png?raw=true "Launch")</a>
1. Click **Next** to proceed with the next step of the wizard.
1. Specify a name and all parameters for the stack.
1. Click **Next** to proceed with the next step of the wizard.
1. Click **Next** to skip the **Options** step of the wizard.
1. Check the **I acknowledge that this template might cause AWS CloudFormation to create IAM resources.** checkbox.
1. Click **Create** to start the creation of the stack.
1. Wait until the stack reaches the state **CREATE_COMPLETE**

![Diagram](./img/S3_AutoLock.png?raw=true "diagram")
