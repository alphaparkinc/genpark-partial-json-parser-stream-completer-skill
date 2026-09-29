# genpark-partial-json-parser-stream-completer-skill

Streaming JSON auto-repair parser balancing quotes, brackets, and key-value colons in real time.

## Architecture

```mermaid
flowchart LR
    Stream["Truncated Streaming JSON: {"a": [1, 2"] --> Scanner[Bracket & Quote Counter]
    Scanner --> Synthesizer[Closing Delimiter Synthesizer]
    Synthesizer --> ValidJSON["Valid Parsed JSON: {"a": [1, 2]}"]
```

## Features
- **Zero-Latency In-Flight Parsing**: Parse live LLM token streams before completion.
- **Pure Python**: 100% Standard Library.
