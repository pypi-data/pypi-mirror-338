# **PyAlert - Email Notifications with Gmail API**

**PyAlert** is a Python-based notification system that allows you to send emails via the **Gmail API** with optional file attachments (up to **5MB**). It ensures emails are still sent even if the file is too large or missing, with a **note** included in the message.

---

## **Features**
- Send email notifications using **Gmail API**  
- Attach files up to **5MB**  
- Automatically **refreshes credentials** when expired  
- **Error handling** for missing or oversized files  
- Includes **notes** in emails when attachments fail  

---

## **Installation & Setup**

### **1. Install Dependencies**
```bash
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### **2. Enable Gmail API & Get Credentials**
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **Gmail API**.
4. Create **OAuth 2.0 Credentials**.
5. Download `credentials.json` and place it in your project folder.

---

## **Usage**

### **Send a Basic Notification**
```python
from pyalert import PyAlert

# Initialize PyAlert
pa = PyAlert(credential="credentials.json", token="token.json")
# Update the sender's address
pa.update_sender("fromsender@gmail.com")
# Update subject line. Default is "PyAlert Notification"
pa.update_subject("New subject")    
# Send an email
pa.push_notification("torecipient@example.com", "Hello! This is a test message.")
```

### **Send an Email with an Attachment**
```python
pa.push_notification("recipient@example.com", "Here's your report!", "report.pdf")
```

### **Send an email-to-text**
You can send **text messages (SMS) and multimedia messages (MMS)** via email using the following [**carrier gateways**](https://github.com/yourusername/pyalert/blob/main/Carriers.md). To send a text message via email, use this format:

```
[10-digit phone number]@[carrier domain]
```

---

## **How It Handles Attachments**
| Scenario | Email Sent? | File Attached? | Additional Note in Email? |
|-----------|------------|---------------|---------------------------|
| Valid file 5MB | Yes | Yes | No extra note |
| File is missing | Yes | No | Yes: "File not found." |
| File is too large (>5MB) |Yes | No | Yes: "File too large." |

---

## **Disclaimer**
This project is provided **"as is"**, without warranty of any kind, express or implied. The author makes no guarantees regarding the accuracy, reliability, or suitability of this software for any particular purpose. 

By using this project, you acknowledge that:
- You are responsible for complying with all applicable laws and regulations, including those related to email-to-text messaging.
- The author is **not liable** for any damages, losses, or issues resulting from the use of this software.
- Carriers may **block, delay, or filter** messages sent via email-to-text gateways.
- The gateways listed may change or be discontinued at any time.

Use this project at your own risk. ðŸš€

---

## **License**
This project is licensed under the **MIT License**.

---
