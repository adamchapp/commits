from git import Repo


def get_commits(repo):
    branch = repo.active_branch
    return list(repo.iter_commits(branch.name))


def read_repo():
    repo = Repo("./")
    commits = get_commits(repo)
    for index, item in enumerate(commits):

        if len(item.parents) > 1:
            print(item.parents)

        #     print("Commit", index, " is a merge", item)
        # else
        #     print("Commit", index, " is not a merge")

read_repo()
