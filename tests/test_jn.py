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
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import unittest

def run_jn(jn, timeout):
    
    open_jn = open(jn, "r", encoding='utf-8')
    notebook = nbformat.read(open_jn, nbformat.current_nbformat)
    open_jn.close()
        
    preprocessor = ExecutePreprocessor(timeout=timeout, kernel_name='python3')
    preprocessor.allow_errors = True    
    preprocessor.preprocess(notebook, {'metadata': {'path': os.path.dirname(jn)}})

    return notebook

def collect_jn_errors(nb):

    errors = []
    for cell in nb.cells:
        if 'outputs' in cell:
            for output in cell['outputs']:
                if output.output_type == 'error':
                    errors.append(output)

    return errors

def embedding_fail(error_list):
    return error_list and 'no embedding found' in error_list

def robust_run_jn(jn, timeout, retries):

    run_num = 1
    notebook = run_jn(jn, timeout)
    errors = collect_jn_errors(notebook)

    while embedding_fail(errors) and run_num < retries:
        run_num += 1
        notebook = run_jn(jn, timeout)
        errors = collect_jn_errors(notebook)

    return notebook, errors

def cell_text(nb, cell):
    return nb["cells"][cell]["outputs"][0]["text"]

jn_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jn_file = os.path.join(jn_dir, '01-structural-imbalance-overview.ipynb')

class TestJupyterNotebook(unittest.TestCase):
    
    def test_jn(self):
        # Smoketest
        MAX_EMBEDDING_RETRIES = 3
        MAX_RUN_TIME = 100

        nb, errors = robust_run_jn(jn_file, MAX_RUN_TIME, MAX_EMBEDDING_RETRIES)

        self.assertEqual(errors, [])

        # Test cell outputs:
        # Section A Toy Example, code cell 1
        self.assertIn("Alice", cell_text(nb, 5))

        # Section A Toy Example, subsection Solving the Problem, code cell 1
        self.assertIn("Yellow", cell_text(nb, 9))

        # Section A Real-World Example, first code cell with output
        self.assertIn("Aleppo", cell_text(nb, 18))

        # Section A Real-World Example, second code cell with text output
        self.assertIn("sign", cell_text(nb, 24))
