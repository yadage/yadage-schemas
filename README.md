# yadage-schemas

[![DOI](https://zenodo.org/badge/54061494.svg)](https://zenodo.org/badge/latestdoi/54061494)
[![PyPI version](https://badge.fury.io/py/yadage-schemas.svg)](https://badge.fury.io/py/yadage-schemas)

[![CI](https://github.com/yadage/yadage-schemas/actions/workflows/ci.yml/badge.svg)](https://github.com/yadage/yadage-schemas/actions/workflows/ci.yml?query=branch%3Amain)

This package holds JSON schema definitions for preserving individual processing tasks of scientific workflows (referred to "packtivities" since they including information where to find their respective prepackage sofware environments) as well as schemas to define declaratively workflows that orchestrate multiple of these steps using directed acyclic graphs (DAGs)

Workflows defined this way can be read and executed by these packages:

* Packtivity: https://github.com/yadage/packtivity
* Yadage: https://github.com/yadage/yadage

