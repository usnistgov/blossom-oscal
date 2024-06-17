# Account Management Workflow
Document that explains the workflow of GitHub actions used to automate account management.

- The **requester** creates a new **GitHub issue** (**Account Request Form**) *to request* an account for the **Account Holder**.
- The **Blossom Management group** is automatically notified *to review* this request through GitHub.
- A **Blossom Management member** reviews the request and *adds a new label* to the issue: ACCOUNT_APPROVED or ACCOUNT_REJECTED
- If **ACCOUNT_APPROVED**, the **Blossom Sysdevs group** is automatically notified to implement the account.
- **Sys-Dev** creates account
- **Sys-Dev** submits a new issue (**Account Management - Authorization Form**) for the Account Holder.

- If **ACCOUNT_REJECTED**, the account request issue is automatically closed.




```mermaid
sequenceDiagram
    actor Rq as Requester
    actor Man as Manager
        
    box Form + Actions
        participant GH as GitHub
    end
    
    box  AWS-Infrastructure
        participant EC2 as EC2-VPC
        participant Cog as CognitoX
    end
    loop Approval Process
        loop Admin Request  
            Rq->>+GH: Creates Account Request
            GH--)+Man: Notifies of Request
            Man--)Man: Reviews Request
            Man->>-GH: Adds Label [ACCOUNT_APPROVED or ACCOUNT_REJECTED]
        end

        loop Implementation
            create actor Sys as Sys-Dev
            GH--)+Sys: On ACCOUNT_APPROVED: 'Creating Account Holder'
            Note left of Sys: Create Account    

            Sys->>Cog: Creates [Account Holder] Record and Attributes
            Sys->>EC2: Registers [Account Holder] With Blockchain
            Note right of Sys: Account Created 

            Sys->>GH: Account Created
        end
    end
    
    Sys->>-GH: Start Account Management - Authorization Form

    create actor AH as Account Holder
    GH--)AH: Maybe Welcome, Created User!

```