# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest

from tests.jn_run import run_jn

jn_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jn_file = os.path.join(jn_dir, '01-structural-imbalance-overview.ipynb')

class TestJupyterNotebook(unittest.TestCase):
    
    def test_jn(self):
        # Smoketest
        nb, errors = run_jn(jn_file)
        self.assertEqual(errors, [])

        # Test cell outputs:
        # Section A Toy Example, code cell 1
        self.assertIn("Alice", nb["cells"][5]["outputs"][0]["text"])

        # Section A Toy Example, subsection Solving the Problem, code cell 1
        self.assertIn("Yellow", nb["cells"][9]["outputs"][0]["text"])

        # Section A Real-World Example, first code cell with output
        self.assertIn("Aleppo", nb["cells"][18]["outputs"][0]["text"])

        # Section A Real-World Example, second code cell with text output
        self.assertIn("sign", nb["cells"][24]["outputs"][0]["text"])

