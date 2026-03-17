# Removing venv from Git tracking

If `venv/` (or `.venv/`, `env/`) was ever committed to this repo, you can stop tracking it **without deleting your local environment**:

```bash
# Stop tracking venv, keep local files
git rm -r --cached venv/

# Commit the change (venv will be removed from the repo, but stays on disk)
git commit -m "chore: stop tracking venv"
```

`.gitignore` already excludes `venv/`, `.venv/`, and `env/`, so they will not be re-added.

**Note:** As of this PR, `venv` is not tracked. This doc exists for future reference or other environments.
