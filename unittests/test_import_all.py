from spinn_front_end_common.utilities import globals_variables

import os
import unittest

import spinn_utilities.package_loader as package_loader


class ImportAllModule(unittest.TestCase):

    def import_module(self, module):
        if os.environ.get('CONTINUOUS_INTEGRATION', 'false').lower() == 'true':
            package_loader.load_module(module,
                                       remove_pyc_files=False)
        else:
            package_loader.load_module(module,
                                       remove_pyc_files=True)

    def test_import_all(self):
        self.import_module("spinn_utilities")
        self.import_module("spinn_machine")
        self.import_module("data_specification")
        self.import_module("spinn_storage_handlers")
        self.import_module("pacman")
        self.import_module("spinnman")
        self.import_module("spinn_front_end_common")
        self.import_module("spynnaker")
        self.import_module("spynnaker7")
        # Avoid safety test that normally prevents importing two simulators
        globals_variables._failed_state = None
        self.import_module("spinnaker_graph_front_end")
        self.import_module("spynnaker_external_devices_plugin")
        self.import_module("spynnaker7_external_devices_plugin")
