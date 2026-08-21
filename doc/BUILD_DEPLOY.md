# Orion-PySDK Build and Deployment

## 1. Purpose and Scope
Orion-PySDK is the Python SDK for the Orion HalService client. The root Makefile uses `uv`, installs `orion-sdk[dev]` editable from `orion-sdk/`, regenerates protobuf/dataclass bindings from the sibling Orion-HAL contracts, and builds wheel/sdist distributions.

## 2. Prerequisites
- Python 3.10 or newer, `uv`, GNU Make, and network access for dependencies.
- Orion-HAL protobuf sources available at the path expected by `tools/gen_proto.py` when regenerating bindings.
- A HalService endpoint and suitable credentials/network for integration use; the repository's unit tests do not establish hardware connectivity.

## 3. Setup
```bash
make setup
make venv
make help
```
`make setup` creates `.venv` with `uv` and installs `orion-sdk[dev]` editable. The install stamp avoids repeating the operation until the environment is removed. `make venv` creates only the environment.

## 4. Build and Compile
```bash
make gen
make gen-check
make build
```
`gen` runs `gen_proto.py` and `gen_types.py`, writing generated output under `orion-sdk/src/orion_sdk/_proto`. `gen-check` regenerates into the working tree, compares committed stubs, and fails if they are stale; run `make gen` and review the diff when that happens. `build` installs the Python `build` package through uv and creates wheel/sdist files in `orion-sdk/dist`.

## 5. Test and Lint
```bash
make test
make lint
make typecheck
make check
```
Tests run pytest with coverage over `orion-sdk/tests`; lint runs Ruff; type checking runs strict mypy using `orion-sdk/pyproject.toml`. `check` is the aggregate lint/typecheck/test gate. Generated proto and type directories are excluded or relaxed by the package's Ruff/mypy configuration.

## 6. Packaging and Artifacts
The supported package command is `make build`. It produces a wheel and source distribution under `orion-sdk/dist`; the package metadata declares runtime `grpcio` and `protobuf` dependencies and optional development tools. There is no registry upload or signed-release target, so publication requires an external credentialed package workflow.

## 7. Deploy, Install, and Run
```bash
make shell
.venv/bin/python -m pip show orion-sdk
```
`make shell` opens a uv-activated subshell. This Makefile does not start a server or install the SDK on a device. Install the built wheel in the consuming application environment and configure its HalService endpoint according to that application's deployment contract. Any target credentials, TLS material, or network routing are external prerequisites.

## 8. Cleanup
```bash
make clean
make distclean
```
`clean` removes package build/dist metadata, test/type/lint caches, coverage output, and Python caches while keeping `.venv`. `distclean` also removes the venv and install stamps.

## 9. Hardware, Cloud, and Manual Verification Caveats
The local test suite validates SDK behavior but does not prove compatibility with a live Orion-HAL service, generated contracts from the deployed server, device permissions, or hardware modules. Manually verify a real gRPC connection, representative HalService calls, error/timeout handling, and version compatibility against the deployed Orion-Client/HAL. No cloud deployment or credentials are managed by this Makefile.
