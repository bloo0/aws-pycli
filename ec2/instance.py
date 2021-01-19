
#!/usr/bin/python3
import boto3, botocore
import os, re
import click

from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv(verbose=True) # LOAD ENV

ARN = os.getenv('MY_ARN')
ROLE_SESSION = os.getenv('MY_ROLE_SESSION')
regions = ['ap-northeast-2','us-east-1'] # Set your regions here

#ec2 = None

def Session():
    sts = boto3.client('sts')
    get_sts = sts.assume_role(RoleArn=ARN,RoleSessionName=ROLE_SESSION)
    return boto3.session.Session(
        aws_access_key_id=get_sts['Credentials']['AccessKeyId'],
        aws_secret_access_key=get_sts['Credentials']['SecretAccessKey'],
        aws_session_token=get_sts['Credentials']['SessionToken']
    )

class AliasedGroup(click.Group):
    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        matches = [x for x in self.list_commands(ctx)
                   if x.startswith(cmd_name)]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))

@click.group(cls=AliasedGroup)
def cli():
    '''
    Helper commands for Ec2 management.
    '''
    pass

@cli.command()
@click.argument('instance_id')
def status(instance_id):
    '''
    Get Instance status
    '''
    global ec2
    session = Session()
    #ec2 = session.resource('ec2', region_name=region)
    for region in regions:
        ec2 = session.resource('ec2', region_name=region)
        instance = ec2.Instance(instance_id)
        print(f'searching [{region}]')
        try:
            status = instance.state['Name']
            print(f'status [{status}]\n')
        except botocore.exceptions.ClientError as error:
            print(f'status [Not Found]\n')
            continue

@cli.command()
@click.argument('instance_id')
def restart_ec2(instance_id):
    '''
    Restart your Instance
    '''
    pass

@cli.command()
@click.argument('instance_id')
def stop_ec2(instance_id):
    '''
    Stop your Instance
    '''
    pass

@cli.command()
@click.argument('instance_id')
def start_ec2(instance_id):
    '''
    Start your Instance
    '''
    pass

@cli.command()
@click.argument('instance_id')
def delete_ec2(instance_id):
    '''
    Delete your Instance
    '''
    pass

if __name__ == '__main__':
    cli()