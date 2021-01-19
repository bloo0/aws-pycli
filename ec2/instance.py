
import boto3, botocore
import os
import click

from dotenv import load_dotenv
from botocore.exceptions import ClientError

# LOAD ENV
load_dotenv(verbose=True)

arn = os.getenv('MY_ARN')
regions = None
ec2 = None

def Session():
    pass

@click.group()
def cli():
    '''
    Helper commands for Ec2 management.
    '''
    pass

@cli.command()
@click.argument('instance_id')
def instance_stat(instance_id):
    '''
    Get ec2 status:
        0 : pending
        16 : running
        32 : shutting-down
        48 : terminated
        64 : stopping
        80 : stopped
    '''
    session = Session()
    ec2 = session.resource()
    instance = ec2.Instance(instance_id)
    status = instance.state()
    return status
    


# restart ec2

# stop ec2

# start ec2

# delete ec2


if __name__ == '__main__':
    cli()