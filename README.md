# Trading Automation Tool (Android Web App)

## Overview

This project is a trading automation tool designed for Android users. It features a floating bar with multiple action buttons, signal extraction from Telegram, Martingale strategy implementation, human-like undetectable automation, and trade win/loss detection. The web app is optimized for Android devices and can be deployed on Zeabur or run locally (Termux or any terminal).

---

## Features

- **Floating Bar UI:** 14 round red action buttons with labels, grouped by category (Buy/Sell, Timeframe, Amount, Signal).
- **Human-like Automation:** Randomized delays, realistic mouse moves/clicks, typing simulation, random empty space clicks.
- **Telegram Signal Extraction:** Fetches signals from up to 5 channels; converts time zones.
- **Martingale Strategy:** Levels per channel, auto-increase/decrease trade amount, reset after win.
- **Trade Detection:** Uses image recognition to confirm win/loss after trades (place `win.png` and `loss.png` in `backend/`).
- **Logging:** All errors and important events are logged for analysis.
- **Android-optimized UI:** Clean, responsive, user-friendly design.
- **Deployment:** Ready for Zeabur cloud or local run on Android/Termux.

---

## File Structure

```
trading-automation-tool/
├── backend/
│   ├── main.py
│   ├── automation.py
│   ├── telegram_signals.py
│   ├── detection.py
│   ├── logger.py
│   └── requirements.txt
├── frontend/
│   ├── public/index.html
│   ├── src/App.jsx
│   ├── src/FloatingBar.jsx
│   ├── src/styles.css
│   └── package.json
├── README.md
└── zeabur.json
```

---

## Local Setup

### Backend

```sh
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```sh
cd frontend
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000) in Chrome on your Android device.

---

## Zeabur Deployment

1. Add your Zeabur project using `zeabur.json` below.
2. Deploy backend and frontend as separate services.
3. Ensure `win.png` and `loss.png` images are placed in the backend directory for trade detection.

---

## Usage

- Use the floating bar to trigger trading actions.
- Backend performs human-like automated trading and signal extraction.
- Trade results are detected and logged.
- All actions optimized for Android device use.

---

## Customization

- Edit `backend/automation.py` for advanced trading logic or to adjust human-like behaviors.
- Edit `frontend/src/styles.css` for UI tweaks.
- Update `backend/logger.py` for different logging outputs.

---

## Troubleshooting

- **Detection not working:** Ensure `win.png` and `loss.png` match your trading platform's result screens and are in the correct directory.
- **Error logs:** See `backend/app.log`.
- **Deployment:** Check Zeabur service logs for startup messages.

---

## License

MIT
