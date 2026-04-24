# SPDX-License-Identifier: MIT
#
# Reproducible-build container for the cross-layer censorship event
# database. Targets IMC / AFT artifact-eval: a single `docker run`
# invocation must reproduce every paper-table number byte-for-byte
# from the committed YAML corpus.
#
# Build:
#   docker build -t p1-event-db:v0.1 .
#
# Reproduce the full derived layer byte-for-byte:
#   docker run --rm -e SOURCE_DATE_EPOCH=1714000000 \
#     -v "$(pwd)":/work p1-event-db:v0.1 make regenerate
#
# Run the fail-closed test suite:
#   docker run --rm p1-event-db:v0.1 make test
#
# Run a one-shot paper-readiness check:
#   docker run --rm -v "$(pwd)":/work p1-event-db:v0.1 make paper-check
#
# Pinning strategy: Python version pinned to 3.12 (matching CI's
# `actions/setup-python@v5 python-version: 3.12`). Third-party deps
# pinned in `requirements.txt` / `requirements-dev.txt`. Git pinned
# only because `scripts/scan_operator_census.py` calls out to it; the
# census is optional and network-dependent so it is NOT part of the
# default reproduction path.

FROM python:3.12.8-slim-bookworm

# Debian's git is only needed for optional operator-census scans;
# the paper-table reproduction path does not touch the network.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git=1:2.39.5-0+deb12u2 \
        make=4.3-4.1 \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work

# Copy the pinning files first so Docker layer-caches the dependency
# install even when source changes.
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the rest of the repo. Exclude large / reproducible-from-upstream
# paths via .dockerignore.
COPY . .

# Default: print the make help (target list) when run without args.
CMD ["make", "help"]
