import time
from flask import request
import json
import os
from pathlib import Path
from datetime import datetime


LOG_DIR = Path.home() /'.slowpoke' / 'logs'
LOG_FILE = LOG_DIR / 'slowpoke.log'

def log_slow_request(request, response, duration):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "method": request.method,
        "route": request.path,
        "status_code": response.status_code,
        "duration_ms": round(duration, 2)
    }


    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")