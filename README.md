# Orion-PySDK

## 1. Project Summary

Orion-PySDK is the Python client library for applications that call the `HalService` endpoint exposed by Orion-Client.

- The distributable package lives in `orion-sdk/` and uses a `src/orion_sdk` layout.
- It provides a Pythonic facade over generated private protobuf and gRPC bindings.
- A caller connects once, discovers modules advertised by the device, obtains a peripheral handle, and invokes one-shot, monitoring, event-based, or long-running work.
- Callers do not construct protobuf messages or handle raw gRPC errors.

The hand-written layer contains channel lifecycle and status-to-exception translation, typed conversion helpers, `Device`, peripheral handles, request builders, session controls, result serialization, and the public exception taxonomy.

- Generated bindings cover shared HAL messages, the service contract, and module packages.
- Descriptor-driven generators produce typed dataclasses and protocol code.
- Examples cover discovery, IMU one-shot and monitoring, event triggers, long-running tests, full self-test, and a small application.

The in-process fake HAL server starts a real gRPC server for tests, so the suite exercises transport and public API together.

- Tests cover connection, discovery, one-shot results, monitoring, event streams, long-running lifecycle, deprecation compatibility, dataclass round trips, and JSON serialization.
- Documentation records the direct-to-Client connection model and contract-version handshake.
- Generated files are private and should be regenerated through the tools.
- Hardware execution and network security remain deployment concerns.

## 2. Feature Status

| # | Name / Description | Implemented? | Test Coverage? | Manual Test |
|---:|---|---|---|---|
| 1 | `orion_sdk.connect()` and persistent gRPC channel | Implemented | Covered by `tests/test_connect.py` | [ ] Manual verification required |
| 2 | Module discovery and peripheral handles | Implemented | Covered by `tests/test_discovery.py` | [ ] Manual verification required |
| 3 | Typed one-shot execution | Implemented | Covered by `tests/test_oneshot.py` | [ ] Manual verification required |
| 4 | Monitoring stream | Implemented | Covered by `tests/test_monitor.py` | [ ] Manual verification required |
| 5 | Event-based trigger stream | Implemented | Covered by `tests/test_event.py` | [ ] Manual verification required |
| 6 | Long-running lifecycle | Implemented | Covered by `tests/test_long_running.py` | [ ] Manual verification required |
| 7 | Typed conversion and JSON output | Implemented | Covered by `tests/test_types_roundtrip.py` | [ ] Manual verification required |
| 8 | gRPC errors translated to `IVVError` | Implemented | Partial: error paths covered | [ ] Manual verification required |
| 9 | Descriptor-driven proto/type generation | Implemented | Partial: generated surface selective | [ ] Manual verification required |
| 10 | Legacy `acadia_sdk` deprecation shim | Implemented | Covered by `tests/test_deprecation_shim.py` | [ ] Manual verification required |
| 11 | Examples and package documentation | Implemented | Unknown: examples not run here | [ ] Manual verification required |

## 3. Build and Test

```bash
cd orion-sdk
make setup
make test
make check
make build
```

See `orion-sdk/docs/quickstart.md`, `docs/api_reference.md`, and `examples/README.md`.
