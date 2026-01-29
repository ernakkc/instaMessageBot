# 💬 Instagram Message Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Instagram](https://img.shields.io/badge/Instagram-Automation-E4405F?style=for-the-badge&logo=instagram&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

*Multi-account Instagram DM automation system with spam protection*

[⚠️ Disclaimer](#️-disclaimer) • [✨ Features](#-features) • [🚀 Quick Start](#-quick-start)

</div>

---

## ⚠️ DISCLAIMER - READ CAREFULLY

**CRITICAL WARNING**:

This tool is provided **FOR EDUCATIONAL PURPOSES ONLY**.

### ❌ PROHIBITED USES:
- Sending unsolicited spam messages
- Violating Instagram Terms of Service
- Harassing or bothering users
- Commercial spamming
- Any illegal activities

### ⚠️ IMPORTANT NOTICES:
- 🚫 **Instagram prohibits automation**
- 🔒 **Account bans are highly likely**
- ⚖️ **May violate anti-spam laws**
- 🚨 **Instagram has strict rate limits**
- 👁️ **Behavior is easily detected**

**THE DEVELOPER:**
- ❌ Does NOT encourage spam or ToS violations
- ❌ Is NOT responsible for account bans
- ❌ Is NOT responsible for legal consequences
- ❌ Provides NO guarantees

**USE AT YOUR OWN RISK. YOU HAVE BEEN WARNED.**

---

## 📖 Overview

Instagram Message Bot is a Python-based automation system that demonstrates multi-account message sending with spam protection. The system supports up to 10 Instagram accounts and includes intelligent rate limiting and data logging.

**Note**: This is an educational project to learn web automation, NOT for actual Instagram marketing.

## ✨ Features

- 👥 **Multi-Account Support**: Manage up to 10 Instagram accounts
- 🎯 **Target Followers**: Send messages to followers of specified accounts
- 🛡️ **Spam Protection**: Built-in rate limiting and delays
- 📊 **Data Logging**: Track all sent messages and activity
- ⏱️ **Smart Delays**: Randomized delays to mimic human behavior
- 💾 **State Persistence**: Save and resume sessions
- 🚦 **Rate Limiting**: Respect Instagram's API limits
- 📄 **Detailed Reports**: CSV logs of all activities

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** installed
- **Chrome Browser**
- **ChromeDriver** (auto-managed)
- Instagram account(s)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ernakkc/instaMessageBot.git
   cd instaMessageBot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure accounts**:
   ```bash
   # Edit config.json with your accounts
   nano config.json
   ```

4. **⚠️ TEST MODE ONLY**:
   ```bash
   python main.py --test
   ```

## ⚙️ Configuration

### config.json Setup

```json
{
  "accounts": [
    {
      "username": "account1",
      "password": "password1",
      "enabled": true
    },
    {
      "username": "account2",
      "password": "password2",
      "enabled": false
    }
  ],
  "targets": [
    "target_username1",
    "target_username2"
  ],
  "message_template": "Hello! This is a test message.",
  "limits": {
    "messages_per_account": 50,
    "messages_per_hour": 20,
    "delay_between_messages": 60
  },
  "settings": {
    "headless": false,
    "test_mode": true,
    "randomize_delays": true
  }
}
```

## 📁 Project Structure

```
instaMessageBot/
├── main.py                # Main script
├── config.json           # Configuration
├── requirements.txt      # Dependencies
├── utils/
│   ├── bot.py            # Bot logic
│   ├── scraper.py        # Follower scraping
│   └── logger.py         # Logging system
├── logs/
│   └── activity.csv      # Activity logs
└── data/
    └── sent_messages.db  # Message database
```

## 🛠️ Dependencies

```txt
selenium>=4.0.0
webdriver-manager>=3.8.0
python-dotenv>=0.19.0
pandas>=1.3.0
```

## 🚫 Instagram Rate Limits

### Official Limits:
- **Follow Actions**: 200-400/day
- **Likes**: 300-1000/day  
- **Comments**: 180-200/day
- **DMs**: 50-100/day per account
- **Hourly Limit**: ~20-30 actions

### Best Practices:
- ✅ Space out actions (60+ seconds)
- ✅ Randomize delays
- ✅ Use multiple accounts
- ✅ Avoid peak hours
- ✅ Gradually increase activity

## 🚨 Safety Recommendations

### Account Protection:
1. **Use Test Accounts**: Never use your main account
2. **Phone Verification**: Have phone numbers ready
3. **Email Backup**: Use accessible email addresses
4. **Proxy Usage**: Consider using proxies
5. **Start Slow**: Begin with minimal activity

### Detection Avoidance:
- ⚠️ Instagram uses ML to detect bots
- ⚠️ IP tracking and device fingerprinting
- ⚠️ Behavioral pattern analysis
- ⚠️ CAPTCHA challenges

## 🐛 Troubleshooting

### Account Locked
```
Solution:
1. Wait 24-48 hours
2. Complete phone/email verification
3. Use more realistic delays
4. Reduce daily activity
```

### ChromeDriver Issues
```bash
pip install --upgrade webdriver-manager
```

### Message Not Sending
```
Possible causes:
- Account action blocked
- Target has DMs disabled
- Network connectivity issues
- Instagram UI changes
```

## 🎯 Ethical Use

This project demonstrates:
- ✅ Web automation techniques
- ✅ Multi-account management
- ✅ Rate limiting implementation
- ✅ Data persistence

### What You Should Know:
1. **Terms of Service**: Read Instagram's ToS
2. **Legal Issues**: Check local automation laws
3. **Account Risk**: High probability of bans
4. **Spam Laws**: CAN-SPAM Act and GDPR
5. **Ethical Marketing**: Respect user privacy

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

**Eren Akkoç**
- 🌐 GitHub: [@ernakkc](https://github.com/ernakkc)
- 📧 Email: ern.akkc@gmail.com

---

<div align="center">

**⚠️ EDUCATIONAL PURPOSE ONLY ⚠️**

**Do NOT use for spam. Respect Instagram's ToS and user privacy.**

**🚫 Automation violates Instagram policies and will result in bans. 🚫**

---

*This project is for learning automation concepts, not for Instagram marketing.*

</div>
