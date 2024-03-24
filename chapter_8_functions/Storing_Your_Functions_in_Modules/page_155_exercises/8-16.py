import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodechedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)


# ----

from printing_functions import print_models
from printing_functions import show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodechedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# ----

from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

unprinted_designs = ['phone case', 'robot pendant', 'dodechedron']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)

# ----

import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodechedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

# ----

from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodechedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)