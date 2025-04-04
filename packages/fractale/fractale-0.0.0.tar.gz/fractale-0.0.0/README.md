# fractale

> Translation layer for a jobspec specification to cluster execution!

[![PyPI version](https://badge.fury.io/py/fractale.svg)](https://badge.fury.io/py/fractale)
[![DOI](https://zenodo.org/badge/773568660.svg)](https://zenodo.org/doi/10.5281/zenodo.13787066)

This library is primarily being used for development for the Fractale project.

## Design

We want to:

1. Generate software graphs for some cluster (fluxion JGF) (this is done with [compspec](https://github.com/compspec/compspec)
2. Register N clusters to a tool (should be written as a python module)
3. Tool would have ability to select cluters from resources known, return 
4. Need graphical reprsentation (json) of each cluster - this will be used with the LLM inference

⭐️ [Documentation](https://compspec.github.io/fractale) ⭐️

Note that the above is not online yet.

## License

HPCIC DevTools is distributed under the terms of the MIT license.
All new contributions must be made under this license.

See [LICENSE](https://github.com/converged-computing/cloud-select/blob/main/LICENSE),
[COPYRIGHT](https://github.com/converged-computing/cloud-select/blob/main/COPYRIGHT), and
[NOTICE](https://github.com/converged-computing/cloud-select/blob/main/NOTICE) for details.

SPDX-License-Identifier: (MIT)

LLNL-CODE- 842614
