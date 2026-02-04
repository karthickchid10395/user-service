# Postman Collection - User Service API Test Guide

## 📦 Collection Overview

The Postman collection `User_Service_API.postman_collection.json` contains **50+ test scenarios** organized into the following categories:

### 1️⃣ Health Checks (2 tests)
- Root endpoint check
- Health endpoint check

### 2️⃣ Success Scenarios (3 tests)
- Valid user registration
- Different country codes
- All special characters in password

### 3️⃣ Validation Errors (13 tests)
- Invalid firstname (contains numbers)
- Invalid lastname (contains special chars)
- Invalid email formats
- Invalid username (special chars)
- Password validation (too short, no special chars, no numbers)
- Password mismatch
- Invalid country code formats
- Invalid mobile number formats

### 4️⃣ Duplicate Checks (3 tests)
- Duplicate username
- Duplicate email
- Duplicate mobile number

### 5️⃣ Missing Fields (4 tests)
- Missing firstname
- Missing email
- Missing password
- Empty request body

### 6️⃣ Boundary Tests (3 tests)
- Minimum length fields
- Maximum mobile number length
- Maximum country code digits

### 7️⃣ Special Cases (4 tests)
- Email with plus sign
- Email with dots
- Whitespace trimming
- Case sensitivity

---

## 🚀 How to Import into Postman

### Method 1: Import File

1. Open **Postman**
2. Click **Import** button (top left)
3. Click **Upload Files**
4. Select `User_Service_API.postman_collection.json`
5. Click **Import**

### Method 2: Drag and Drop

1. Open **Postman**
2. Drag `User_Service_API.postman_collection.json` into Postman window
3. Collection will be imported automatically

---

## ⚙️ Configuration

### Set Base URL

The collection uses a variable `{{baseUrl}}` which is set to `http://localhost:7566` by default.

**To change the port or host:**

1. Click on the collection name in Postman
2. Go to **Variables** tab
3. Change the value of `baseUrl`
4. Click **Save**

**Common configurations:**
```
Development:  http://localhost:7566
Production:   https://api.yourservice.com
Docker:       http://localhost:8000
```

---

## 🧪 Running Tests

### Run Individual Test

1. Expand the collection folders
2. Click on any request
3. Click **Send** button
4. View response in the bottom panel

### Run All Tests in a Folder

1. Right-click on a folder (e.g., "Validation Errors")
2. Click **Run folder**
3. Click **Run** button
4. View test results

### Run Entire Collection

1. Right-click on collection name
2. Click **Run collection**
3. Click **Run User Service API**
4. View comprehensive test results with pass/fail status

---

## 📊 Test Execution Order

### Recommended Order for Manual Testing:

1. **Health Checks** - Verify service is running
2. **Success Scenarios** - Create initial valid users
3. **Duplicate Checks** - Test duplicate validation (uses data from step 2)
4. **Validation Errors** - Test all field validations
5. **Missing Fields** - Test required field validation
6. **Boundary Tests** - Test edge cases
7. **Special Cases** - Test special scenarios

---

## ✅ Expected Results

### Success Response (201 Created)
```json
{
  "message": "User created successfully"
}
```

### Validation Error (422 Unprocessable Entity)
```json
{
  "detail": [
    {
      "type": "string",
      "loc": ["body", "firstname"],
      "msg": "Value error, First name must contain only alphabetic characters",
      "input": "John123"
    }
  ]
}
```

### Duplicate Error (400 Bad Request)
```json
{
  "message": "Validation error",
  "errorInfo": {
    "detail": "Username already exists"
  }
}
```

---

## 🎯 Test Scenarios Breakdown

### Firstname Validation
- ✅ Valid: `"John"`, `"Jane"`
- ❌ Invalid: `"John123"`, `"John@"`, `"J"`

### Lastname Validation
- ✅ Valid: `"Doe"`, `"Smith"`
- ❌ Invalid: `"Doe123"`, `"Doe@123"`, `"D"`

### Email Validation
- ✅ Valid: `"john@example.com"`, `"test+tag@example.com"`
- ❌ Invalid: `"invalidemail.com"`, `"test@"`, `"@example.com"`

### Username Validation
- ✅ Valid: `"johndoe123"`, `"user456"`
- ❌ Invalid: `"john@doe"`, `"user_name"`, `"ab"`

### Password Validation
- ✅ Valid: `"SecurePass@123"`, `"Pass@123!Word#"`
- ❌ Invalid: `"pass"`, `"Password123"`, `"Pass@word"`
- Must have: 8+ chars, letters, numbers, special chars (@$!%*#?&)

### Country Code Validation
- ✅ Valid: `"+1"`, `"+91"`, `"+44"`, `"+9999"`
- ❌ Invalid: `"1"`, `"+1a"`, `"++1"`

### Mobile Number Validation
- ✅ Valid: `"1234567890"`, `"123456789012345"`
- ❌ Invalid: `"123"`, `"12345abc90"`, `"12345"`

---

## 📝 Test Data Template

Use this template for creating new test cases:

```json
{
  "firstname": "John",
  "lastname": "Doe",
  "email": "unique.email@example.com",
  "username": "uniqueusername123",
  "password": "SecurePass@123",
  "confirmpassword": "SecurePass@123",
  "countrycode": "+1",
  "mobilenumber": "9876543210"
}
```

**Remember to use UNIQUE values for:**
- email
- username
- countrycode + mobilenumber combination

---

## 🔍 Automated Test Scripts

Some requests include automated test scripts that verify:

- HTTP status codes (201, 400, 422, 500)
- Response message content
- Error information presence
- Response structure

**View test results in:**
- Postman → Send request → Test Results tab (bottom panel)

---

## 🐛 Troubleshooting

### Collection Won't Import
- Ensure JSON file is not corrupted
- Try Method 2 (drag and drop)
- Check Postman version (use latest)

### Requests Failing with Connection Error
- Verify service is running: `http://localhost:7566/health`
- Check `baseUrl` variable matches your server
- Ensure no firewall blocking the port

### All Validation Tests Passing When They Shouldn't
- Database might not have initial data
- Run "Success Scenarios" folder first
- Clear database and retest

### Tests Show Different Status Codes
- Check your schema validators in code
- Verify error handling in `user_routes.py`
- Review console logs in application

---

## 💡 Tips for Effective Testing

1. **Run Health Checks First** - Ensure service is running
2. **Create Valid Users** - Run success scenarios to populate database
3. **Test Duplicates** - Use exact same data as successful registrations
4. **Clean Database** - Reset between full test runs for consistency
5. **Monitor Server Logs** - Watch console for detailed error messages
6. **Use Collection Runner** - Run entire collection for regression testing
7. **Export Results** - Save test run results for documentation

---

## 📊 Collection Statistics

- **Total Requests**: 32
- **Test Categories**: 7
- **Automated Tests**: 3 (with test scripts)
- **Validation Scenarios**: 13
- **Success Scenarios**: 3
- **Duplicate Tests**: 3
- **Edge Cases**: 7

---

## 🔄 Continuous Testing

### Using Newman (Postman CLI)

Install Newman:
```bash
npm install -g newman
```

Run collection:
```bash
newman run User_Service_API.postman_collection.json
```

With environment:
```bash
newman run User_Service_API.postman_collection.json --env-var "baseUrl=http://localhost:7566"
```

---

## 📚 Additional Resources

- **API Documentation**: http://localhost:7566/docs
- **OpenAPI Spec**: http://localhost:7566/openapi.json
- **ReDoc**: http://localhost:7566/redoc

---

**Happy Testing! 🎉**

For issues or questions, refer to the project README.md or check application logs.

