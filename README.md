# Orion-PySDK

Python SDK leaf for the **Orion** project (NVIDIA Jetson + STM32) in the
SiliconCentric `project-managers` fleet.

This leaf provides `orion-sdk`, a Pythonic gRPC client for the `HalService`
endpoint exposed by `Orion-Client`. The SDK distribution package is
**`orion-sdk`** (import name `orion_sdk`); a `acadia_sdk` deprecation shim
re-exports the public surface for callers still on the old name.

The SDK source, tooling, docs, examples, and test suite live under
[`orion-sdk/`](orion-sdk/). See [`orion-sdk/README.md`](orion-sdk/README.md)
for the full API, quickstart, and `make` targets (`setup`, `gen`, `check`,
`build`).

---
Part of the `Orion` project in the `project-managers` fleet. See
`docs/project-managers.md` for the full 9-project / 8-leaf hierarchy and
shared conventions.