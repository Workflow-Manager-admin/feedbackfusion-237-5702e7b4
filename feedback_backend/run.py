from app import app
from app.models import init_db
from app.config import Config


def _get_host_port_from_base_url(base_url):
    """Extract host & port from BASE_URL if possible, else use Flask default."""
    try:
        import urllib.parse
        parsed = urllib.parse.urlparse(base_url)
        host = parsed.hostname or "127.0.0.1"
        port = int(parsed.port) if parsed.port else 5000
    except Exception:
        host, port = "127.0.0.1", 5000
    return host, port


if __name__ == "__main__":
    init_db()
    host, port = _get_host_port_from_base_url(Config.BASE_URL)
    print(f"Running Flask app at http://{host}:{port}")
    app.run(host=host, port=port)
