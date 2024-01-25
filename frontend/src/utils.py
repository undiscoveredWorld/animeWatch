def prepare_url(url: str) -> str:
    if url.endswith("/"):
        return url
    else:
        return url + "/"
