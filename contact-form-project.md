
# 🛠️ AWS Project: Serverless Contact Form with Notifications and Monitoring

This project builds a **secure, serverless contact form backend** using multiple AWS services. The focus is on wiring services together with **minimal code**, relying mostly on AWS configurations and integrations.

---

## 🎯 Project Goal

Create a contact form backend that:
- Accepts POST submissions (name, email, message)
- Saves each submission to DynamoDB
- Sends email notifications via SNS
- Logs every submission and error
- Monitors the system for failures
- Uses rate limiting and IAM for security

Estimated time to complete: **~4 hours** (all within AWS Free Tier)

---

## 📦 Services Involved

| AWS Service      | Purpose                           |
|------------------|-----------------------------------|
| API Gateway      | REST API for contact form         |
| Lambda           | Processing and glue logic         |
| DynamoDB         | Store contact submissions         |
| SNS              | Email notifications + monitoring  |
| CloudWatch       | Logs + error monitoring           |
| IAM              | Role-based access control         |
| (Optional) WAF   | Protect API Gateway from abuse    |

---

## 🧩 Task Breakdown

### 1. Create the API Layer (API Gateway)
- Create a REST API with resource `/contact` and method `POST`
- Enable **Lambda Proxy Integration**
- Use **Request Models + Mapping Templates** to validate required fields: `name`, `email`, `message`

### 2. Lambda Function (Glue Logic)
- Triggered by API Gateway
- Parses request, creates UUID for message ID
- Stores item in DynamoDB
- Publishes message to SNS topic
- Logs input and errors to CloudWatch

### 3. DynamoDB Table
- Table Name: `contact_messages`
- Partition Key: `message_id` (String)
- Attributes: `name`, `email`, `message`, `timestamp`

### 4. SNS Topic (Notifications)
- Topic: `contact-form-alert`
- Subscribe an email address (must confirm subscription)
- Lambda publishes to this topic on every new contact message

### 5. Monitoring with CloudWatch
- Enable Lambda logging
- Create **CloudWatch Alarm** to monitor:
  - API Gateway 5xx errors or
  - Lambda failures
- Alarm triggers SNS (could be same topic or separate)

### 6. Security and Abuse Protection
- Use IAM roles with **least privilege**
- Lock down API Gateway with **Usage Plans + API Key** (free tier friendly)
- Optionally use **AWS WAF** for:
  - Rate limiting
  - Geo-blocking
  - ReCaptcha challenge

---

## 🧪 Bonus (Optional)
- Enable **X-Ray tracing** for Lambda
- Export CloudWatch Logs to S3
- Add reCAPTCHA verification to form input (integrated on frontend)

---

## 🔐 Security Checklist

- [ ] Use IAM roles for Lambda with scoped permissions (`PutItem`, `Publish`)
- [ ] DynamoDB is not public
- [ ] SNS only accessible by Lambda and alert systems
- [ ] API Gateway has rate limits via Usage Plans
- [ ] Log everything including failures
- [ ] Monitor and alert on suspicious activity

---

## 🔧 Troubleshooting

### ❌ Error: `Missing Authentication Token`
- Likely cause: wrong endpoint path or method not deployed

### ❌ SNS not sending emails
- Check if the email subscription is **confirmed**

### ❌ Lambda fails with `AccessDeniedException`
- Add missing permissions to Lambda's IAM role (`dynamodb:PutItem`, `sns:Publish`)

### ❌ No logs in CloudWatch
- Ensure Lambda logging is enabled and it's being triggered

### ❌ API Gateway input validation not working
- Recheck your **Mapping Template** and request model

---

## ⏱️ Estimated Time Allocation

| Task                    | Time Estimate |
|-------------------------|---------------|
| Setup & Deployment      | 2 hours       |
| IAM & Security Config   | 1 hour        |
| Testing & Troubleshooting | 1 hour     |

---

## 🧭 Outcome

This project gives you hands-on experience with building a **real-world serverless architecture** on AWS using only Free Tier eligible services. It's a perfect exercise to show understanding of AWS integrations, security best practices, and observability.

