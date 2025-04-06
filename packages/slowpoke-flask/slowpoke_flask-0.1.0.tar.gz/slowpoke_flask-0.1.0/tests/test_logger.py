from slowpoke.logger import log_slow_request
from pathlib import Path
import json

class DummyRequest:
    method = "POST"
    path = "/submit"

class DummyResponse:
    status_code = 201

def test_log_slow_request(tmp_path, monkeypatch):
    fake_log_file = tmp_path / "slowpoke.log"
    fake_log_dir = fake_log_file.parent

    monkeypatch.setattr("slowpoke.logger.LOG_FILE", fake_log_file)
    monkeypatch.setattr("slowpoke.logger.LOG_DIR", fake_log_dir)

    log_slow_request(DummyRequest(), DummyResponse(), 123.45)

    assert fake_log_file.exists()
    logs = fake_log_file.read_text().strip().split("\n")
    assert len(logs) == 1

    entry = json.loads(logs[0])
    assert entry["method"] == "POST"
    assert entry["route"] == "/submit"
    assert entry["status_code"] == 201
    assert entry["duration_ms"] == 123.45
