import click
import yaml
from datetime import datetime

@click.command()
@click.option('--user-username', required=True, help='Username of user to delete')
@click.option('--issue-number', help='Issue number of user account deletion request')
@click.option('--ssp-path', help='File path of SSP to update')
@click.option('--requester', help='Username of GitHub user that created account deletion request')
@click.option('--approver', help='Username of GitHub user that approved account deletion request')
@click.option('--session-id', help='Session ID')
def delete_user(user_username, issue_number, ssp_path, requester, approver, session_id):
    """
    Creates a yaml file containing information about a user to delete

    Args:
        user_username (string): String containing username of user to delete
        issue_number (string): String containing issue number of user account deletion request
        ssp_path (string): String containing file path of SSP to update
        requester (string): String containing username of GitHub user that created account deletion request
        approver (string): String containing username of GitHub user that approved account deletion request
        session_id (string): String containing session ID
    """
    
    # Structure of yaml file
    cmd = {
    "command" : "delete-user",
    "user" : {
        "username" : f"{user_username}",
        "ssp-path": f"{ssp_path}",
        "requester": f"{requester}",
        "approver": f"{approver}",
        },
    }
    
    # Include timestamp in filename
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Write to user yaml file (stored in repo)
    filename = "ops/secops/deleted_users/" + timestamp + "_deleted_user.yaml"
    with open(filename, 'w') as f:
        print(f"\n\n{yaml.safe_dump(cmd, default_flow_style=False)}", file=f)
        
    # Structure of yaml file referencing user yaml file
    reference = {
        "file": f"{filename}",
        "issue_number": f"{issue_number}",
        "branch_name": f"{session_id}"
    }
    
    # Write to user reference yaml file (sent to S3)
    filename_reference = "ops/secops/reference_deleted_users/" + timestamp + "_reference_user.yaml"
    with open(filename_reference, 'w') as f:
        print(f"\n\n{yaml.safe_dump(reference, default_flow_style=False)}", file=f)

if __name__ == '__main__':
    delete_user()