def decode_uri(base_url: str, url_data: str) -> str:
    decode = {
        "!": "%21",
        "#": "%23",
        "$": "%24",
        "&": "%26",
        "'": "%27",
        "(": "%28",
        ")": "%29",
        "*": "%2A",
        "+": "%2B",
        ",": "%2C",
        "/": "%2F",
        ":": "%3A",
        ";": "%3B",
        # "=": "%3D",
        "?": "%3F",
        "@": "%40",
        "[": "%5B",
        "]": "%5D",
        "\n": "%0A",
        " ": "%20",
        '"': "%22",
        "%": "%25",
        # "-": "%2D",
        # ".": "%2E",
        "<": "%3C",
        ">": "%3E",
        # "\\": "%5C",
        "^": "%5E",
        # "_": "%5F",
        "`": "%60",
        "{": "%7B",
        "}": "%7D",
        "|": "%7C",
        "~": "%7E",
    }

    new_str = ''
    for c in url_data:
        if c in decode.keys():
            c = decode[c]

        new_str += c
    return base_url + 'json=' + new_str


if __name__ == '__main__':
    some_url_with_json = "https: // api.supermetrics.com/enterprise/v2/query/data/json?"
    dict_credentials = {"ds_id": "SOME", "ds_accounts": ["123456"], "ds_user": "email@mail.combr", "api_key": "your_api_key"}"
    full_url = decode_uri(
        some_url_with_json, str(dict_credentials).replace("'", '"').replace(' ', ''))

    print(full_url)
