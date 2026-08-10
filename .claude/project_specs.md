# Orion-PySDK — specs Remote: `git@github.com:SiliconCentric/Orion-PySDK.git`
Stack: Python, uv-managed, src layout. Consumes the `HalService` gRPC endpoint exposed by Orion-Client — the same wire contract
Orion-Server speaks. ## Layout * `orion-sdk/` — everything: source, tooling, docs, examples, the make workflow (setup/ gen/ check/ build).
* `orion-sdk/src/orion_sdk/` — the package. Import name `orion_sdk`, distribution name `orion-sdk`.
* `orion-sdk/src/orion_sdk/_proto/` and `types/` — generated stubs, ~270 files, **committed on purpose**.
* `acadia_sdk` — deprecation shim re-exporting the public surface for callers on the old name. Lazy PEP 562 `__getattr__`, emits a `DeprecationWarning`, ships in the wheel. ## The regeneration exception This is the one leaf that regenerates protos. Orion-Client and Orion-Server must not, because a
second copy of the generated C++ symbols causes ODR/duplicate-symbol link errors. That is a C++
constraint with no Python equivalent, so it does not apply here.
