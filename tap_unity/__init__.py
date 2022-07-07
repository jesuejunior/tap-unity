#!/usr/bin/env python3
import singer
from singer import utils
from runner import TapUnityRunner


REQUIRED_CONFIG_KEYS = ["config"]
LOGGER = singer.get_logger()


@utils.handle_top_exception(LOGGER)
def main():
    # Parse command line arguments
    args = utils.parse_args(REQUIRED_CONFIG_KEYS)

    runner = TapUnityRunner()

    # If discover flag was passed, run discovery mode and dump output to stdout
    if args.discover:
        catalog = runner.discover()
        catalog.dump()
    # Otherwise run in sync mode
    else:
        if args.catalog:
            catalog = args.catalog
        else:
            catalog = runner.discover()
        runner.do_sync(args.config, args.state, catalog)


if __name__ == "__main__":
    main()
