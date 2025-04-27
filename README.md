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
CHANNEL_ID=your channel ID, e.g. -1001234567890
```
<p>4. Run application</p>

```bash
uvicorn main:app --host 0.0.0.0 --port 5000
```
