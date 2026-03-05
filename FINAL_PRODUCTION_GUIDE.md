# 🚀 Disposition Extraction Model: Technical Production Guide (v2.0)

This is the all-in-one technical reference for the **khushianand01/disposition_model** and its associated API.

---

## 🏗️ 1. Architecture & Engine
- **Base Model**: Qwen-2.5-7B-Instruct (Fine-tuned for Hinglish/Multilingual Debt Collection).
- **Quantization**: 4-bit (bitsandbytes) for high performance on Tesla T4 GPUs.
- **Inference Stack**: FastAPI + Unsloth (2x faster than standard Transformers).
- **Communication**: Supports both **REST (HTTP 1.1)** and **WebSockets** for real-time extraction.

---

## 📊 2. Performance Metrics (Round 8)
*   **Disposition Accuracy**: **81.5%** (Meets production co-pilot standards).
*   **JSON Integrity**: **100% Valid** (Zero structural crashes).
*   **Date Reliability**: **100% Accurate** (Relative dates parso/kal are resolved correctly).
*   **PTP Recall**: **62.0%** (Identifies the majority of payment commitments).

### 🏆 Precision Highlights (Zero False Positives)
The model is **100% accurate** (Precision = 1.0) and safe for direct automation in these areas:
- **WANT_FORECLOSURE** / **SETTLEMENT**
- **SWITCHED_OFF** / **OUT_OF_NETWORK** / **WRONG_NUMBER**
- **WILL_PAY_AFTER_VISIT** (Field pickup requests)

---

## ⚖️ 3. Scalability & Concurrency
Powered by a single **Tesla T4 (16GB)** GPU on the current server.

| Metric | Threshold | Verdict |
| :--- | :--- | :--- |
| **Direct Parallelism** | **1 Request** | Queuing lock ensures 100% safety. |
| **Concurrency (Queued)** | **5+ Users** | Handled with incremental queue delay (~20s max). |
| **Average Latency** | **~4.5s** | Single user, warm model. |

---

## 🛠️ 4. Operational Control Commands
Run these from the `/home/ubuntu/disposition_model/disposition_websockets` directory.

*   **START (Background)**:
    ```bash
    nohup /home/ubuntu/disposition_model/venv/bin/python3 app.py > api_ws.log 2>&1 &
    ```
*   **STOP**:
    ```bash
    sudo fuser -k 8005/tcp
    ```
*   **RESTART**:
    ```bash
    sudo fuser -k 8005/tcp && nohup /home/ubuntu/disposition_model/venv/bin/python3 app.py > api_ws.log 2>&1 &
    ```
*   **MONITOR LATEST LOGS**:
    ```bash
    tail -f api_ws.log
    ```

---

## 🧠 5. Key Logic & New Features
- **Family Member Detection**: Automatically detects son, wife, or relative and labels as `ANSWERED_BY_FAMILY_MEMBER`.
- **Medical Emergencies**: Brand new `MEDICAL_ISSUE` label for identifying health-related payment denials.
- **Job Loss**: Specifically maps job changes and layoffs to `JOB_CHANGED_WAITING_FOR_SALARY`.
- **Smart UI Dashboard**: Paste an entire JSON block into the UI transcript box—it will auto-detect it and clean the text for you.

---
*Status: STABLE / PRODUCTION READY*  
*Location: http://65.0.97.13:8005*
