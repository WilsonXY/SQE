# Cross-model writing experiments

Repeats of the three-condition writing experiment (raw, Humanizer, pstack technical-writing + unslop) described in `../WRITING-EXPERIMENT-PROTOCOL.md`. The original GPT-6.1-Sol run lives in `../report/assignment-1/`.

| Run | Model | Design | Start here |
|---|---|---|---|
| `claude-opus-5-5/run-1` | Claude Opus 5.5 (Claude Code) | Own raw per model; close replication of the agent arrangement | `claude-opus-5-5/run-1/run-record.md`, then `review/comparison.md` |

`tools/count_words.py` reproduces the original run's counting method (4,873 on the original raw files) and similarity measure. `tools/check_protected.py` compares protected elements against a frozen raw draft.
