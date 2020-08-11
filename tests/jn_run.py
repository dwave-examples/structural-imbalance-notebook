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

def run_jn(jn):
    
    open_jn = open(jn, "r")
    notebook = nbformat.read(open_jn, nbformat.current_nbformat)
    open_jn.close()
        
    preprocessor = ExecutePreprocessor(timeout=100, kernel_name='python3')
    preprocessor.allow_errors = True    
    preprocessor.preprocess(notebook, {'metadata': {'path': os.path.dirname(jn)}})

    errors = []
    for cell in notebook.cells:
        if 'outputs' in cell:
            for output in cell['outputs']:
                if output.output_type == 'error':
                    errors.append(output)

    return notebook, errors

 

