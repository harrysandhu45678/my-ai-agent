import webbrowser


WEBSITES = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "github": "https://github.com",
    "gmail": "https://mail.google.com",
}


def open_website(site):

    site = site.lower()

    if site in WEBSITES:
        webbrowser.open(WEBSITES[site])
        return f"Opening {site.title()}."

    return None