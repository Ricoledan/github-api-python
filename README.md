# github-api-python

## Summary
This Python script uses the PyGithub library and GitHub API to collect data from a list of specified GitHub
repositories. It retrieves and counts the number of contributors and releases in the past year for each repository,
storing this data in a pandas DataFrame. If the script exceeds the GitHub API's rate limit, it prints an error message
and stops processing. The final output is a DataFrame listing the repository name, the number of contributors, and the
number of releases in the past year for each repository. The part of the script intended to find 'active' contributors (
those with more than 50 commits in the past year) is commented out.

## Usage
Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Run Python Script

```bash
python main.py
```