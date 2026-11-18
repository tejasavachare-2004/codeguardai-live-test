import subprocess


def run_user_command(command: str) -> str:
    """Run a command supplied by the user."""
    return subprocess.check_output(
        command,
        shell=True,
        text=True
    )


if __name__ == "__main__":
    user_input = input("Enter command: ")
    print(run_user_command(user_input))