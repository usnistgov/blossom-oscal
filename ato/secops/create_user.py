import click
import yaml
from datetime import datetime

@click.command()
@click.option('--user-name', required=True, help='Name of user to create')
@click.option('--user-email', required=True, help='Email of user to create')
@click.option('--user-role', required=True, help='Role of user to create')
@click.option('--location-uuid', help='UUID of physical location of user')
@click.option('--org-member', help='UUID of organization that user is member of')
@click.option('--issue-number', help='Issue number of user account request')
def create_user(user_name, user_email, user_role, location_uuid, org_member, issue_number):
    """
    Creates a yaml file containing information about a new user

    Args:
        user_name (string): String containing name of new user
        user_email (string): String containing email of new user
        user_role (string): String containing role of new user
        location_uuid (string): String containing UUID of physical location of user
        org_member (string): String containing UUID of organization that user is member of
        issue_number (string): String containing issue number of user account request
    """
    
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
    
    # Write to user yaml file (stored in repo)
    filename = "ato/oscal-artifacts/created_users/created_user_" + timestamp + ".yaml"
    with open(filename, 'w') as f:
        print(f"\n\n{yaml.safe_dump(cmd, default_flow_style=False)}", file=f)
        
    # Structure of yaml file referencing user yaml file
    reference = {
        "file": f"{filename}",
        "issue_number": f"{issue_number}",
        "branch_name": f"account-request-{issue_number}"
    }
    
    # Write to user reference yaml file (sent to S3)
    filename_reference = "ato/oscal-artifacts/reference_created_users/reference_created_user_" + timestamp + ".yaml"
    with open(filename_reference, 'w') as f:
        print(f"\n\n{yaml.safe_dump(reference, default_flow_style=False)}", file=f)

if __name__ == '__main__':
    create_user()