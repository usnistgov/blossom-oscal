# Account Management Workflow

This document explains the workflow of GitHub actions used to automate Blossom service's accounts management.

## Account Request and Creation
- [ ] The requester requests an account for the Account Holder by creating a new GitHub issue using the Account Request Form.
- [ ] The Blossom Management group is automatically notified to review the request through GitHub.
- [ ] One of the Blossom Management (a member of the Blossom Management group) reviews the request and adds a new label to the issue: ACCOUNT_APPROVED or ACCOUNT_REJECTED
- [ ] If ACCOUNT_REJECTED, the account request issue is automatically closed.
- [ ] If the account is approved and the label ACCOUNT_APPROVED is added, the Blossom Sysdevs group is automatically notified to implement the account.
- [ ] Upon completion of creating the account requested, the Blossom Sysdev links the Account Request issue to the Pull Request that implements the account.
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
