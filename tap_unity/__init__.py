#!/usr/bin/env python3
import singer
from singer import utils as singer_utils
from tap_unity.runner import TapUnityRunner


REQUIRED_CONFIG_KEYS = ["auth_token", "organization_id"]
LOGGER = singer.get_logger()


@singer_utils.handle_top_exception(LOGGER)
def main():
    args = singer_utils.parse_args(REQUIRED_CONFIG_KEYS)

    runner = TapUnityRunner(
        config=args.config,
        state=args.state,
    )
    runner.sync()


if __name__ == "__main__":
    main()
