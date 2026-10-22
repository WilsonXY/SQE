# Skill provenance — run claude-opus-5-5/run-1

Same installed files as the GPT-6.1-Sol run, verified by SHA-256 on 22 October 2026 before any agent started:

| Skill | Path | SHA-256 | Matches protocol §5 |
|---|---|---|---|
| humanizer (3.1.0) | `C:/Users/xingy/.codex/skills/humanizer/SKILL.md` | `0612f1dfb1672b0ea9b97e139bf1f06cabe98d8b27424fe8ff01e1fb4cc99cad` | Yes |
| technical-writing | `C:/Users/xingy/.codex/skills/technical-writing/SKILL.md` | `61fe9c424a798ebf36ad94941f87be049cb8827bdf86d21474a0dde37b513c43` | Yes |
| unslop | `C:/Users/xingy/.codex/skills/unslop/SKILL.md` | `ccab208e315ce05e2fab8eeee2f7879f1289b5c6844840b2d307adf31c79144f` | Yes |

The skills are loaded by reading the `SKILL.md` file directly, not through a slash command; Claude Code's own skill registry does not list these three.

## Visible but unused

Claude Code lists a separate user skill, `wilson-humanizer` (`~/.claude/skills/wilson-humanizer`). It is a different instruction file and is **not** the treatment. All agents are told not to use it. Its name and one-line description are visible to every agent in this harness. As in the original run, skill names were visible, so the raw condition is protected by instruction rather than by absence.
