# Git and GitHub Practice

This repository is created to learn and practise Git and GitHub concepts through hands-on exercises.

## Topics Covered

- Git basics and version control
- Branching and merging
- Git remote repositories
- Fetch and pull
- Merge conflicts
- GitHub Pull Requests
- GitHub Issues
- Merge vs Rebase

## Git Branching and Pull Request Workflow

This section explains a basic Git collaboration workflow using feature branches and GitHub Pull Requests.

### 1. Create a Feature Branch

Start by creating a separate branch for your new feature or task.

```bash
git switch main
git pull origin main
git switch -c feature/feature-name
```

Working on a separate branch keeps changes isolated from the main branch.

### 2. Make Changes and Commit

After making changes to your files, check the working tree:

```bash
git status
```

Stage and commit your changes:

```bash
git add .
git commit -m "Describe your changes"
```

A commit records a snapshot of your changes in Git history.

### 3. Push the Feature Branch

Push your branch to GitHub:

```bash
git push -u origin feature/feature-name
```

The `-u` option sets the upstream tracking branch, making future pushes easier.

### 4. Create a Pull Request

On GitHub:

1. Open the repository.
2. Select the Pull Requests tab.
3. Click New Pull Request.
4. Select `main` as the base branch.
5. Select your feature branch as the compare branch.
6. Add a descriptive title and explanation.
7. Create the Pull Request.

A Pull Request allows other developers to review your changes before they are integrated into the main branch.

### 5. Review and Merge the Pull Request

Before merging:

- Review the changed files.
- Check the proposed changes.
- Run automated tests and CI checks, if configured.
- Address review comments and requested changes.

Once approved and all required checks pass, merge the Pull Request using the strategy selected by the project.

Common GitHub merge strategies:

- Create a merge commit
- Squash and merge
- Rebase and merge

### 6. Clean Up Branches

After the Pull Request has been merged, delete the remote feature branch using GitHub or:

```bash
git push origin --delete feature/feature-name
```

Delete the local branch:

```bash
git switch main
git pull origin main
git branch -d feature/feature-name
```

This keeps the repository organized by removing branches that are no longer needed.

## Useful Git Commands

| Command | Purpose |
|---|---|
| `git status` | Check working tree status |
| `git branch` | List local branches |
| `git switch branch-name` | Switch branches |
| `git switch -c branch-name` | Create and switch to a branch |
| `git add .` | Stage changes |
| `git commit -m "message"` | Create a commit |
| `git push` | Push commits |
| `git fetch` | Download remote updates |
| `git pull` | Fetch and integrate remote updates |
| `git merge branch-name` | Merge another branch into the current branch |
| `git rebase branch-name` | Rebase the current branch onto another branch |
| `git log --oneline --graph --all` | Visualize commit history |

## Learning Objective

The objective of this repository is to build practical knowledge of Git and GitHub workflows, including version control, collaboration, code reviews, and maintaining a clean project history.