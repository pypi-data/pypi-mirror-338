def test_shell_cmd(gitprune):
    shell_cmd = gitprune.shell_cmd("echo testing123")
    assert shell_cmd == "testing123"
    assert isinstance(shell_cmd, str)


def test_get_remote_branches(gitprune):
    remote_branches = gitprune.remote_branches
    assert "master" in remote_branches
    assert isinstance(remote_branches, list)
    assert remote_branches != []


def test_local_branches(gitprune):
    local_branches = gitprune.local_branches
    assert "setup" in local_branches
    assert isinstance(local_branches, list)
    assert local_branches != []


def test_not_remote(gitprune):
    assert isinstance(gitprune.not_remote, list)
    assert gitprune.not_remote == ["setup"]


def test_delete_branches(gitprune):
    gitprune.shell_cmd("git branch new-branch")
    gitprune.shell_cmd("git branch main")
    assert (
        "new-branch" in gitprune.local_branches
    ), "new-branch was not found after being created"
    gitprune.shell_cmd("git checkout new-branch")
    assert (
        "new-branch" in gitprune.not_remote
    ), "new-branch not appearing as a local only branch"
    gitprune.delete_branches()
    assert (
        "new-branch" not in gitprune.local_branches
    ), f"{gitprune} still showing locally after attempting to delete local branches"
