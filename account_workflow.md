# Account Management Workflow

This document explains the workflow of GitHub actions used to automate Blossom service's accounts management.

## Account Request and Creation
-[ ] The requester requests an account for the Account Holder by creating a new GitHub issue using the Account Request Form.
-[ ] The Blossom Management group is automatically notified to review the request through GitHub.
-[ ] One of the Blossom Management (a member of the Blossom Management group) reviews the request and adds a new label to the issue: ACCOUNT_APPROVED or ACCOUNT_REJECTED
-[ ] If the account is approved and the label ACCOUNT_APPROVED is added, the Blossom Sysdevs group is automatically notified to implement the account.
-[ ] Upon completion of creating the account requested, the Blossom Sysdev submits a new GitHub issue using the Account Management Authorization Form for the Account Holder.
-[ ] If ACCOUNT_REJECTED, the account request issue is automatically closed.

## Account Disable
[TBD]

## Account Enable
[TBD]

## Account Change
[TBD]

## Account Deletion
[TBD]
