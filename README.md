# Falling Pickaxe
Falling Pickaxe Game inspired from YouTube shorts livestreams.

## 🇻🇳 Hướng dẫn nhanh (Quick Start for Vietnamese Users)

Để chạy game, bạn chỉ cần mở PowerShell tại thư mục này và chạy:
```powershell
./scripts/run.ps1
```

### Các lỗi thường gặp:
*   **Lỗi Execution Policy (Không chạy được script):** Chạy lệnh sau để cấp quyền:
    ```powershell
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass
    ```
*   **Lỗi SSL khi cài Pygame:** Nếu dùng Python 3.14+, hãy mở `requirements.txt` và đổi `pygame` thành `pygame-ce==2.5.7`.

---

## 🇺🇸 English Guide

### Before you use it
If you consider streaming this game on your own youtube channel, please add credits in the description of your video/livestream. 

### Quick Start (Recommended)
The easiest way to run the game is using the automated scripts that handle everything for you:

**For Windows:**
```powershell
./scripts/run.ps1
```

**For Linux/macOS:**
```bash
chmod +x ./scripts/run.sh
./scripts/run.sh
```

These scripts will automatically:
- Create a Python virtual environment if it doesn't exist
- Install all required dependencies
- Run the game with automatic restart on crashes
- Exit cleanly when you close the game window

### Manual Setup (Advanced Users)
If you prefer to set up the environment manually:

1. Make sure you have Python 3.x installed.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```
3. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the game:
   ```bash
   python ./src/main.py
   ```

## 🛠 Troubleshooting / Sửa lỗi

### 1. PowerShell Script Error (Execution Policy)
**Issue:** `...cannot be loaded because running scripts is disabled on this system.`
**Solution:**
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass
```

### 2. Pygame SSL/Build Error
**Issue:** Errors during `pip install` related to SSL certificates or building wheels for `pygame`.
**Solution:** Switch to `pygame-ce`.
1. Open `requirements.txt`.
2. Change `pygame==...` to `pygame-ce==2.5.7`.
3. Run the start script again.

---

## ⚙️ Configuration (Optional)
1. Make a copy of `default.config.json` to `config.json`.
2. Create your Google API Key for YouTube and enable YouTube Data API v3.
3. Set your `CHANNEL_ID` and `LIVESTREAM_ID` in `config.json`.
4. Set `"CHAT_CONTROL": true` to enable YouTube integration.

### Available chat commands
`tnt`, `fast`, `slow`, `big`, `wood`, `stone`, `iron`, `gold`, `diamond`, `netherite`

### MegaTNT Spawning
- Triggered by new subscribers (detected via API polling).
- Polling frequency: `YT_POLL_INTERVAL_SECONDS`.
- Manual spawn: Press `M` key.

---

**Falling Pickaxe: Ultimate Mining Arcade Game for Streamers!**

Step into the world of **Falling Pickaxe**, the most addictive and interactive mining arcade game designed specifically for YouTube streamers! Let your viewers control the game via live chat commands and super chats.

- **Interactive Live Chat Integration:** Let viewers spawn TNT or change your pickaxe!
- **Explosive Visuals:** Stunning particle effects and physics.
- **Monetization:** Perfect for Super Chat interactions.
