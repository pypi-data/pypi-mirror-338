import argparse

def argParseDriver(
    keywords,
    required=[],
    defaults={}
):
    parser = argparse.ArgumentParser()
    for keyword in keywords:
        keyword = '--' + keyword.strip('-')
        parser.add_argument(
            keyword,
            required=True if keyword.strip('-') in required else None,
            default=defaults[keyword.strip('-')] if keyword.strip('-') in defaults.keys() else None
        )
    return parser.parse_args()