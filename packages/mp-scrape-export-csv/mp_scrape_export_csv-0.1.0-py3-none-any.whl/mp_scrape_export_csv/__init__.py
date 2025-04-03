# SPDX-FileCopyrightText: 2025 Sofía Aritz <sofiaritz@fsfe.org>
#
# SPDX-License-Identifier: AGPL-3.0-only

from mp_scrape_core import DataConsumer, ModuleDefinition, ModuleDescription, ModuleArgument, ModuleMaintainer
import pandas as pd

import logging

class CsvExport(DataConsumer):
    def __init__(self, dest = "result.csv", index = True):
        """
        Export the data in a CSV file

        :param str dest: (Destination file) Where will the CSV file be stored.
        :param bool index: (Keep index) When enabled, the index will be kept.
        """
        self.dest = dest
        self.index = index

    @staticmethod
    def metadata() -> ModuleDefinition:
        return ModuleDefinition({
            "name": "CSV export",
            "identifier": "csv",
            "description": ModuleDescription.from_init(CsvExport.__init__),
            "arguments": ModuleArgument.list_from_init(CsvExport.__init__),
            "maintainers": [
                ModuleMaintainer({
                    "name": "Free Software Foundation Europe",
                    "email": "mp-scrape@fsfe.org"
                }),
                ModuleMaintainer({
                    "name": "Sofía Aritz",
                    "email": "sofiaritz@fsfe.org"
                }),
            ]
        })
    
    async def consume(self, logger: logging.Logger, data: pd.DataFrame) -> None:
        data.to_csv(self.dest, index=self.index)