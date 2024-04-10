#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_custom_appsflyer import SourceCustomAppsflyer

if __name__ == "__main__":
    source = SourceCustomAppsflyer()
    launch(source, sys.argv[1:])
