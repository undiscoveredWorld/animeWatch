def return_response_or_raise_exception(response):
    if response:
        return response
    else:
        raise RuntimeError("Got None object")
