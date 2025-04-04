# Muscle

# Copyright <2015-2025> <Université catholique de Louvain (UCLouvain)>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# List of the contributors to the development of Muscle: see NOTICE file.
# Description and complete License: see NOTICE file.

"""
Displacement Method (DM) solvers for structural analysis.

This package contains linear and nonlinear displacement method solvers for structural analysis.
"""

from .linear_dm import main_linear_displacement_method
from .nonlinear_dm import main_nonlinear_displacement_method

__all__ = ['main_linear_displacement_method', 'main_nonlinear_displacement_method']
