import subprocess
from slowpoke.logger import LOG_FILE
from pathlib import Path

def test_cli_report(tmp_path, monkeypatch, capsys):
    log_path = tmp_path / "slowpoke.log"
    monkeypatch.setattr("slowpoke.logger.LOG_FILE", log_path)
    monkeypatch.setattr("slowpoke.logger.LOG_DIR", tmp_path)

    # Create a dummy log entry
    log_path.write_text('{"method": "GET", "route": "/", "status_code": 200, "duration_ms": 150}\n')

    from slowpoke.cli import report
    report()

    out = capsys.readouterr().out
    assert "GET" in out
    assert "/" in out
    assert "200" in out
