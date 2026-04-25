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
#   docker run --rm -e SOURCE_DATE_EPOCH="$(git log -1 --format=%ct)" \
#     -v "$(pwd)":/work p1-event-db:v0.1 make regenerate
#
# Run the fail-closed test suite:
#   docker run --rm p1-event-db:v0.1 make test
#
# Run a one-shot paper-readiness check:
#   docker run --rm -v "$(pwd)":/work p1-event-db:v0.1 make paper-check
#
# Pinning strategy: the base image is pinned by both tag and sha256
# digest (set the digest below at release-tag time; until then the
# tag alone is used, with a comment naming the build-time digest).
# Third-party Python deps pinned in `requirements*.txt`. Debian apt
# packages are intentionally NOT version-pinned: Debian rotates point
# releases out of the apt index in months, which breaks
# image rebuilds for an artifact-eval reviewer 6+ months
# post-submission. We capture the actual installed versions to a
# receipts file at build time so the reproduced versions are
# auditable without locking the rebuild to a specific point release.

# When tagging a Zenodo release, set the digest below by replacing the
# tag-only `python:3.12.8-slim-bookworm` with the
# `python:3.12.8-slim-bookworm@sha256:<digest>` form (see
# https://hub.docker.com/_/python for the digest of the desired tag).
FROM python:3.12.8-slim-bookworm

# `git` is only used by the optional operator-census scanner;
# `make` drives the build targets. Both are unpinned by version on
# purpose (see header comment); the actual installed versions are
# recorded to `/build-receipts.txt` for auditability.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        make \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && { \
        echo "# build receipts"; \
        echo "python: $(python3 --version 2>&1)"; \
        echo "git:    $(git --version 2>&1)"; \
        echo "make:   $(make --version 2>&1 | head -1)"; \
        echo "debian: $(cat /etc/debian_version 2>&1)"; \
    } > /build-receipts.txt

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
