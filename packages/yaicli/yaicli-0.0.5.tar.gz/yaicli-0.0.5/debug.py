import typer

app = typer.Typer()


@app.command()
def run(name: str):
    """
    这是 run 命令的简短描述。

    这是详细的帮助信息，同样可以写多行。
    这个命令会运行主要的任务。
    """
    print(f"正在为 {name} 运行任务...")


# 注意：如果这是唯一的命令，它的帮助信息会比较突出。
# 如果还有其他命令，这只是 'run' 命令的帮助。
# 应用的总体帮助需要通过 Typer(help=...) 设置。

if __name__ == "__main__":
    app()
