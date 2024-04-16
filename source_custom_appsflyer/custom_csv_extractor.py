import csv
import io
from typing import Any, List, Mapping

import requests
from airbyte_cdk.sources.declarative.extractors.record_extractor import RecordExtractor


class CustomCSVExtractor(RecordExtractor):
    """
    Record extractor that extracts records from a CSV response.

    This extractor assumes that the CSV response is returned as bytes.

    Attributes:
        config (Config): The user-provided configuration as specified by the source's spec
    """

    def extract_records(self, response: requests.Response) -> List[Mapping[str, Any]]:
        if not isinstance(response.content, bytes):
            raise ValueError("Response content is not bytes.")
        
        records = []
        print('status_code', response.status_code)
        csv_str = response.content.decode('utf-8')
    
        # Use StringIO to create a file-like object for CSV module
        csv_file = io.StringIO(csv_str)
        
        # Parse the CSV data
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            records.append(row)

        return records
