# difftags

- RB-0001: first commit
- RB-0002: commit
- Rb 0003: commit
- RB-0004: commit
- RB 0005: commit
- RB-0006: commit
- RB-0007: commit
- RB-0008: commit
- RB 0009: commit
- Rb 0010: commit
- RB-0011: commit


```
git log v0.3...v0.1
git log v0.3...v0.1 --oneline
git rev-list v0.3...v0.1 --oneline
git log --pretty=oneline `git tag --sort=-committerdate | head -1`...`git tag --sort=-committerdate | head -2 | tail -1` |cut -d " " -f 2-
git log --pretty=format:%s `git tag --sort=-committerdate | head -1`...`git tag --sort=-committerdate | head -2 | awk '{split($0, tags, "\n")} END {print tags[1]}'` > change_log.txt
git log --pretty=format:"%h; author: %cn; date: %ci; subject:%s" v0.1...v0.2
git log --pretty=format:"author: %cn; subject:%s" v0.3...v0.1
```