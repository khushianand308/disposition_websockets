# 📞 Disposition Extraction API - Version 2.0 (Production)

A high-performance production package for extracting structured **Call Dispositions**, **Payment Intent**, and **Reason for Not Paying** from conversational transcripts.

![Status](https://img.shields.io/badge/Status-Production-success)
![Version](https://img.shields.io/badge/Version-2.0.0-green)
![Model](https://img.shields.io/badge/Model-Qwen%202.5%207B%20(4--bit)-blue)
![Stack](https://img.shields.io/badge/Stack-Unsloth%20%7C%20FastAPI-blueviolet)

---

## 📁 Project Structure
This repository contains the optimized, clean production assets:

```
disposition_websockets/
├── api/                            # core service implementation
│   ├── app.py                      # FastAPI server
│   ├── inference.py                # inference engine (Unsloth)
│   └── static/                     # web UI dashboard
├── app.py                          # root wrapper
├── requirements.txt                # production dependencies
├── disposition_api.service         # systemd unit file
└── PRODUCTION_HANDOVER_v2.md      # detailed deployment guide
```

---

## 🛠️ Hardware Requirements
*   **GPU:** Minimum **15GB VRAM** (Tesla T4, A10, A30, or A100).
*   **VRAM Usage:** ~14.1 GB.
*   **Memory:** 16GB+ System RAM.

---

## ⚙️ Installation & Running

### 1. Manual Execution & Quick Controls
```bash
# ----- START -----
# Option A: Standard (Interactive)
python3 app.py

# Option B: Background (Recommended for manual server use)
nohup venv/bin/python3 app.py > api_ws.log 2>&1 &

# ----- STOP & FREE GPU -----
# 1. Try to kill the web process gracefully:
sudo fuser -k 8005/tcp

# 2. Force-kill zombie python processes to free GPU VRAM (if nvidia-smi shows remaining processes):
sudo pkill -9 -f "python3 app.py"
# Alternatively, find the PID in nvidia-smi and run: sudo kill -9 <PID>

# ----- RESTART -----
# Kill and then start in background
sudo fuser -k 8005/tcp && nohup venv/bin/python3 app.py > api_ws.log 2>&1 &

# ----- MONITOR -----
# Check real-time logs
tail -f api_ws.log
```
*   **Dashboard**: `http://localhost:8005`
*   **Health**: `http://localhost:8005/health`

### 2. Production Service (systemd)
```bash
# Update the path in the .service file if your folder is not /home/ubuntu/
sudo cp disposition_api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable disposition_api
sudo systemctl start disposition_api
```

---

## 📮 API Testing (Postman)
*   **REST (POST)**: `http://65.0.97.13:8005/predict`
    *   Body: `raw/JSON` -> `{"transcript": "Agent: hello, Borrower: will pay 5000 next monday"}`
*   **WebSocket**: `ws://65.0.97.13:8005/ws`
    *   Message: `{"transcript": "Agent: hello, Borrower: i lost my job i cannot pay"}`

---

## 📝 Recommended Transcript Format
For maximum accuracy, provide the transcript as a conversation:  
`Agent: [Question/Statement] Borrower: [Customer Response]`

---

## 📊 Deployment Benchmarks
| Single User | 3 Concurrent Users | 5 Concurrent Users |
| :--- | :--- | :--- |
| **~4.5s Latency** | ~12.5s Latency | ~22.2s Latency |

*Note: The API handles parallel requests by queuing them safely to prevent GPU OOM crashes.*

---

## 🌐 Intent Extraction Logic
- **Job Loss Mapping**: Automatically maps "I lost my job" or "no work" to `JOB_CHANGED_WAITING_FOR_SALARY`.
- **Dynamic Dates**: Resolves relative terms (*kal, parso*) into standard `YYYY-MM-DD` using the server's real-time clock.
- **Multilingual Support**: Supports Hindi, Bengali, English, Marathi, Tamil, Telugu, Gujarati, Kannada, Malayalam, and Punjabi.

---

## 📑 Support & Documentation
For a full breakdown of the accuracy metrics and deployment details, see: [PRODUCTION_HANDOVER_v2.md](./PRODUCTION_HANDOVER_v2.md)
