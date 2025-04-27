<h1>Email Tracking Pixel</h1>
<a href="https://github.com/justrals/email-tracking-pixel-tg"><img src="https://img.shields.io/github/stars/justrals/email-tracking-pixel-tg" height="25px"></a>

<h2>What's that?</h2>
<p>It's a script that tracks email read status and sends alerts via Telegram Bot API.</p>
<h2>Installation</h2>
<p>You should have Python 3.7 or higher installed before proceeding.</p>

<p>1. Clone the repository</p>

```bash
git clone https://github.com/justrals/email-tracking-pixel-tg.git
cd email-tracking-pixel-tg
```
<p>2. Install dependencies</p>

```bash
pip install -r requirements.txt
```
<p>3. Create .env file with the following content</p>

```bash
TOKEN=your API token from @BotFather
CHAT_ID=your chat ID, e.g. 12345670
```
<p>4. Run application</p>

```bash
uvicorn main:app --host 0.0.0.0 --port 5000
```

<h2>Usage</h2>

<p>1. <b>Encode</b> the email address in Base64.</p>

<p>2. <b>Set</b> this URL as an image attachment in your mailing app:</p>

```
http://your-server-ip:5000/seen?e=<base64-encoded-email>
```

<p><b>Done!</b> Alerts will be sent to Telegram when the email is opened.</p>
