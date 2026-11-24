import pytest

from services.env_check import validate_env


def test_validate_env_rejects_missing_admin_key(monkeypatch):
    monkeypatch.delenv("ADMIN_KEY", raising=False)
    assert validate_env(strict=False) is False


def test_validate_env_accepts_configured_admin_key(monkeypatch):
    monkeypatch.setenv("ADMIN_KEY", "test-only-admin-key")
    assert validate_env(strict=False) is True


def test_validate_env_aborts_startup_without_admin_key(monkeypatch):
    monkeypatch.delenv("ADMIN_KEY", raising=False)
    with pytest.raises(SystemExit) as exc:
        validate_env(strict=True)
    assert exc.value.code == 1
