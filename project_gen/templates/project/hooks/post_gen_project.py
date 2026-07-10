import subprocess


def init_poetry():
    subprocess.run(["poetry", "install", "--no-root"])


def init_pre_commit():
    subprocess.run(["poetry", "add", "pre-commit"], check=True)
    subprocess.run(["poetry", "run", "pre-commit", "install"], check=True)
    subprocess.run(["poetry", "run", "pre-commit", "autoupdate"], check=True)


if __name__ == "__main__":
    init_poetry()
    init_pre_commit()
