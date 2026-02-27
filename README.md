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
└── PRODUCTION_HANDOVER_v1.md      # detailed deployment guide
```

---

## 🛠️ Hardware Requirements
*   **GPU:** Minimum **15GB VRAM** (Tesla T4, A10, A30, or A100).
*   **VRAM Usage:** ~14.1 GB.
*   **Memory:** 16GB+ System RAM.

---

## ⚙️ Installation & Running

### 1. Simple manual start
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```
*   **Dashboard**: `http://localhost:8005`
*   **Health**: `http://localhost:8005/health`

### 2. Production Service (systemd)
```bash
sudo cp disposition_api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable disposition_api
sudo systemctl start disposition_api
```

---

## 📊 Deployment Benchmarks
| Single User | 3 Concurrent Users | 5 Concurrent Users |
| :--- | :--- | :--- |
| **~4.5s Latency** | ~12.5s Latency | ~22.2s Latency |

*Note: The API handles parallel requests by queuing them safely to prevent GPU OOM crashes.*

---

## 🌐 Intent Extraction Logic
- **Job Loss**: Maps intents to `JOB_CHANGED_WAITING_FOR_SALARY`.
- **Date Handling**: Resolves relative terms (*kal, parso*) into standard `YYYY-MM-DD` using the server's real-time clock.
- **Multilingual**: High accuracy across Hindi, Bengali, English, Marathi, Tamil, Telugu, and more.

---

## 📑 Support & Documentation
For a full breakdown of the accuracy metrics, see: [PRODUCTION_HANDOVER_v1.md](./PRODUCTION_HANDOVER_v1.md)
