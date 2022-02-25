from typing import Callable, Dict, Optional, Set

# This is used to keep track of all handlers requiring
# authentication, and the token types/prefixes each of
# them allows.
handlers_auth: Dict[Callable, Set[Optional[str]]] = {}
