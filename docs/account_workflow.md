# Account Management Workflow

This document explains the workflow of GitHub actions used to automate Blossom service's accounts management.

## Requirements to run Actions
- [ ] Repository secrets: AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, AWS_BUCKET
- [ ] Issue labels: ACCOUNT_REQUEST_RECORD, ACCOUNT_APPROVED, ACCOUNT_REJECTED, ACCOUNT_IMPLEMENTED

## Account Request and Creation
- [ ] The requester requests an account for the Account Holder by creating a new GitHub issue using the Account Request Form.
- [ ] The Blossom Management group is automatically notified to review the request through GitHub.
- [ ] One of the Blossom Management (a member of the Blossom Management group) reviews the request and adds a new label to the issue: ACCOUNT_APPROVED or ACCOUNT_REJECTED
- [ ] If ACCOUNT_REJECTED, the account request issue is automatically closed.
- [ ] If the account is approved and the label ACCOUNT_APPROVED is added, the Blossom Sysdevs group is automatically notified about implementation.
- [ ] A YAML file is automatically created from information submitted through the Account Request Form, which is pushed to the GitHub repo as a new branch and a condensed version is sent to S3 bucket.
- [ ] S3 bucket receives the file about the new user to create and sends a trigger to EC2, which implements the new user in Cognito, SSM, ACL, AMB as necessary.
- [ ] The new user is inserted into the SSP, which is pushed into the GitHub repo to the new branch.
- [ ] Upon completion of creating the account requested, a Pull Request is automatically created, to link the branch with the Account Request issue.
- [ ] Upon merging the Pull Request that implements the account, the relevant updated controls are re-assessed automatically. The Blossom Assessors group is then notified to monitor the automated assessment.
- [ ] TBD: STEPS FOR AUTOMATED ASSESSMENT

## Account Disable
[TBD]

## Account Enable
[TBD]

## Account Change
[TBD]

## Account Deletion
[TBD]
