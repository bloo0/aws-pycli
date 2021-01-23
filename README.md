aws-pycli
==============================

Manage your AWS Services via Python

Getting Started
------------

1. Install the following python module:
- `pip install click`
- `pip install python-dotenv`
- `pip install termcolor`

2. Setup AWS Assume Role
3. Add your AWS Regions
4. Set your environmental variables

How to use:
------------
```sh
./instance.py status <your_instance_id>
```

list Commands:
- `delete-ec2   Delete your Instance`
- `list-ec2     Get list of instances`
- `restart-ec2  Restart your Instance`
- `start-ec2    Start your Instance`
- `status       Get Instance status`
- `stop-ec2     Stop your Instance`


Future updates
------------
1. Add other AWS Services to manage
2. Add console message status