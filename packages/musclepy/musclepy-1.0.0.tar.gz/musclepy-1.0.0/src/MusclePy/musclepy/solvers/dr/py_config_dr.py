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

class PyConfigDR:
    """
    Configuration parameters for the Dynamic Relaxation method.
    
    This class contains all the parameters needed to control the behavior of the
    Dynamic Relaxation algorithm, including time step, mass parameters, and
    termination criteria.
    """
    
    def __init__(self, dt=0.01, mass_ampl_factor=1, min_mass=0.005, max_time_step=10000, max_ke_reset=1000, zero_residual_rtol=1e-4, zero_residual_atol=1e-6):
        """
        Initialize the Dynamic Relaxation configuration.
        
        Args:
            dt: [s] - Time step for the time incremental method
            mass_ampl_factor: Amplification factor for the fictitious masses
            min_mass: [kg] - Minimum mass applied to each DOF if null stiffness is detected
            max_time_step: Maximum number of time steps before termination
            max_ke_reset: Maximum number of kinetic energy resets before termination
            zero_residual_rtol: Relative tolerance for zero residual check, compared to external loads magnitude
            zero_residual_atol: Absolute tolerance (in N) for zero residual check, when loads are near zero
        """
        # Mass parameters
        self.mass_ampl_factor = mass_ampl_factor if mass_ampl_factor > 0 else 1  # Amplification factor for masses
        self.min_mass = min_mass if min_mass > 0 else 0.005  # [kg] - Minimum mass for each DOF
        self.huge_mass = 1e15  # [kg] - Mass applied to fixed DOFs
        
        # Time step parameters
        self.dt = dt if dt > 0 else 0.01  # [s] - Time step
        
        # Termination criteria
        self.max_time_step = max_time_step if max_time_step > 0 else 10000  # Maximum number of time steps
        self.max_ke_reset = max_ke_reset if max_ke_reset > 0 else 1000  # Maximum number of kinetic energy resets
        self.zero_residual_rtol = zero_residual_rtol if zero_residual_rtol > 0 else 1e-4  # Relative tolerance for zero checks
        self.zero_residual_atol = zero_residual_atol if zero_residual_atol > 0 else 1e-6  # Absolute tolerance (in N) for zero checks

        # Initialize counters, to be returned to the user for information regarding the solver performances.
        self.n_time_step = 0  # Number of time steps performed
        self.n_ke_reset = 0  # Number of kinetic energy resets performed