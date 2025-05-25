
# 🚀 AWS Project: Professional Serverless Contact Form System (Multi-Service Architecture)

This project demonstrates how to design a **production-ready, serverless, event-driven architecture** on AWS using managed services with minimal code. The system showcases strong understanding of **integration, observability, and security** in the AWS cloud.

---

## 🧠 Use Case

You're tasked with building a secure, scalable backend for a contact form on a public-facing website. The solution must log submissions, send alerts, handle retries and errors, and be secured against abuse — all while staying within AWS Free Tier.

---

## 🧩 Architecture Overview

**Services Involved (8+):**

| AWS Service      | Role in System                                         |
|------------------|--------------------------------------------------------|
| API Gateway      | Front-facing REST API to receive form submissions      |
| Lambda           | Main processor for incoming requests                   |
| DynamoDB         | Stores contact form messages with metadata             |
| SNS              | Sends email alerts on new submission                   |
| SQS (DLQ)        | Captures failed Lambda executions                      |
| CloudWatch       | Logs, metrics, and alarms for monitoring               |
| IAM              | Role-based access controls and service permissions     |
| WAF              | Protects API Gateway from bots and common attacks      |
| X-Ray (Optional) | Tracing for performance and bottleneck analysis        |
| S3 (Optional)    | Backup submissions or exported logs                    |

---

## 🛠️ Key Features

- **Fully Serverless:** No infrastructure to maintain.
- **Event-Driven:** Automatically responds to form submissions.
- **Fail-Safe:** Failed executions are sent to a dead-letter queue (SQS).
- **Auditable:** Logs and metrics are available in CloudWatch.
- **Secure:** Rate limits, WAF rules, and IAM policies applied.
- **Real-Time Notification:** Emails sent instantly using SNS.

---

## ✅ Requirements Checklist

| Capability                         | Implemented with                          |
|-----------------------------------|-------------------------------------------|
| Accept HTTP POST requests         | API Gateway                               |
| Serverless function trigger       | Lambda                                    |
| Data storage                      | DynamoDB                                  |
| Notification on new entry         | SNS Email                                 |
| Secure access                     | API Key + WAF + IAM                       |
| Monitoring                        | CloudWatch Logs + Alarms                  |
| Retry/failure handling            | SQS DLQ for Lambda                        |
| Service-to-service permissioning  | IAM Roles + Policies                      |

---

## 🗂️ Step-by-Step Tasks

### 1. REST API (API Gateway)
- Create a REST API with a POST `/contact` method.
- Enable **Lambda Proxy integration**.
- Use **Request Validation** to ensure required fields.

### 2. Lambda Function (Python)
- Generates a UUID for the message ID.
- Saves data to DynamoDB.
- Publishes an SNS message.
- Logs input and status to CloudWatch.
- Add error handling and send to SQS on failure.

### 3. DynamoDB Table
- Table name: `contact_messages`
- Partition key: `message_id` (String)
- Other attributes: `name`, `email`, `message`, `timestamp`

### 4. SNS Topic
- Name: `contact-alerts`
- Add an email subscription.
- Ensure email confirmation.

### 5. SQS Queue (Dead Letter Queue)
- Configure Lambda to send failures to an SQS DLQ.
- Set up alert if DLQ receives messages.

### 6. CloudWatch Monitoring
- Log all Lambda invocations.
- Create metrics filters for errors.
- Alarm on Lambda error count > 1 in 5 minutes.

### 7. IAM Security
- Create dedicated IAM roles for Lambda.
- Grant **least privilege**: only `PutItem`, `Publish`, etc.

### 8. WAF Protection
- Add WAF WebACL to API Gateway.
- Rules to block bots, common attacks (e.g. SQLi, XSS).
- Optional: rate limit or captcha challenge.

### 9. (Optional) X-Ray Tracing
- Enable X-Ray on Lambda for tracing.

### 10. (Optional) Export Logs to S3
- Create subscription filter to push logs to S3 for audit/archive.

---

## 🔐 Security Checklist

- [x] API key enabled for POST method.
- [x] WAF added to restrict IPs or block bad patterns.
- [x] IAM roles scoped per service.
- [x] DLQ captures failed executions.
- [x] CloudWatch alarm notifies on Lambda failures.
- [x] HTTPS enforced by default via API Gateway.

---

## 📦 Deliverables

- Source code for Lambda function
- `README.md` with full instructions and API usage
- Screenshots of API Gateway, DynamoDB, and SNS working (if demoing)
- Link to GitHub/GitLab repository

---

## 🧪 Sample Payload

```json
{
  "name": "Ali",
  "email": "ali@example.com",
  "message": "I would like to get in touch."
}
```

---

## 🧪 PowerShell Test

```powershell
$uri = "https://your-api-id.execute-api.region.amazonaws.com/dev/contact"
$headers = @{
    "Content-Type" = "application/json"
    "x-api-key" = "your-api-key-here"
}
$body = '{
  "name": "Ali",
  "email": "ali@example.com",
  "message": "This is a test message"
}'

$response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body
$response
```

---
