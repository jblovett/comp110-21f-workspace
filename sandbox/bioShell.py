import subprocess
import asyncio


def main() -> None:
    print("hi")


def bio_process(shell_id: str, shell_password: str, args: list[str] = []) -> None:
    
    ssh = subprocess.Popen(["ssh", shell_id],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True,
                           bufsize=0)

    ssh.stdin.write(shell_password)

    for line in ssh.stdout:
        print(line.strip())


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('ssh jblovett@152.19.198.95'))
