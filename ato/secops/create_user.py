import click
import yaml
from datetime import datetime

@click.command()
@click.option('--user-name', required=True, help='Name of user to create')
@click.option('--user-email', required=True, help='Email of user to create')
@click.option('--user-role', required=True, help='Role of user to create')
@click.option('--location-uuid', help='UUID of physical location of user')
@click.option('--org-member', help='UUID of organization that user is member of')
def create_user(user_name, user_email, user_role, location_uuid, org_member):
    # Structure of yaml file
    cmd = {
    "command" : "create-acl-user|create-cognito-user",
    "user" : {
        "name" : f"{user_name}",
        "email-address":f"{user_email}",
        "role":f"{user_role}",
        "location-uuid":f"{location_uuid}",
        "member-of-organization":f"{org_member}",
        },
    }
    
    # Include timestamp in filename
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = "ato/oscal-artifacts/created_users/created_user_" + timestamp + ".yaml"

    # Write to yaml file
    with open(filename, 'w') as f:
        print(f"\n\n{yaml.safe_dump(cmd, default_flow_style=False)}", file=f)

if __name__ == '__main__':
    create_user()