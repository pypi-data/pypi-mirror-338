# -*- coding: utf-8 -*-

import os
import sys
import logging



# Add testing solution project source path
here = os.path.abspath(os.path.dirname(__file__))
source_path = os.path.normpath(os.path.join(here, 'src'))
sys.path.insert(0, source_path)


# Add HolAdo project paths
# holado_path = os.getenv('HOLADO_PATH')
holado_path = None
if holado_path is None:
    from holado import get_holado_path
    holado_path = get_holado_path()
sys.path.insert(0, holado_path)
sys.path.insert(0, os.path.join(holado_path, "src") )
sys.path.insert(0, os.path.join(holado_path, "tests", "behave") )


# Configure HolAdo
import holado
from context.session_context import TSSessionContext
# holado.initialize(TSessionContext=TSSessionContext, 
holado.initialize(TSessionContext=None, 
                  logging_config_file_path=os.path.join(here, 'logging.conf'), log_level=logging.INFO,
                  garbage_collector_periodicity=None)


# Import generic environment methods
from behave_environment import *

# Define project specific environment methods
# TestConfig.profile_memory_in_features = True
# TestConfig.profile_memory_in_scenarios = True



