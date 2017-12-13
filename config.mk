# Variables for Makefile

# Name of the environment .yml file
ENV_YML=environment.yml

GRAPHICS=$(wildcard results/*.png)
RESULTS=$(wildcard results/*)

SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = TestSphinxSite
SOURCEDIR     = .
BUILDDIR      = _build