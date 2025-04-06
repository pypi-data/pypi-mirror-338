import time
from flask import Flask
from pathlib import Path
import json

from slowpoke.core import monitor

def test_monitor_logs_slow_request(tmp_path, monkeypatch):
    fake_log_file = tmp_path / "slowpoke.log"
    monkeypatch.setattr("slowpoke.logger.LOG_FILE", fake_log_file)
    monkeypatch.setattr("slowpoke.logger.LOG_DIR", tmp_path)

    app = Flask(__name__)
    monitor(app)

    @app.route("/slow")
    def slow():
        time.sleep(0.15)  # 150ms > 100ms default threshold
        return "slow response"

    with app.test_client() as client:
        client.get("/slow")

    assert fake_log_file.exists()

    logs = fake_log_file.read_text().strip().split("\n")
    assert len(logs) >= 1
    entry = json.loads(logs[0])
    assert entry["method"] == "GET"
    assert entry["route"] == "/slow"
    assert entry["status_code"] == 200
    assert entry["duration_ms"] > 100
