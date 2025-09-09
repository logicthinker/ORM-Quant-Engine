# Agent Guardrails

This repository describes guardrails and expectations for automated agents, such
as OpenAI Codex, that make changes to the codebase.

## Rules

1. **Test–Driven Development (TDD) Only**. All features must start with
   failing tests. Agents should never add functionality without first
   codifying acceptance criteria in tests.
2. **Strict static analysis**. Code must type-check with `mypy --strict` and
   pass `ruff` linting. Add type hints and fix lint warnings before
   submission.
3. **Purity and determinism**. Functions in `src/orm_engine` must be pure,
   performing no I/O or network calls during tests. Randomness must be
   controlled via explicit parameters or determinism.
4. **Named constants**. Avoid magic numbers. Introduce named constants for
   regulatory factors or calibration knobs and document their meaning.
5. **Definition of Done**. A pull request is ready when:
   - All tests pass in CI.
   - Coverage of changed lines is at least 90% (measured via pytest-cov).
   - A brief design note summarizing assumptions and known limitations is
     included in the PR description.