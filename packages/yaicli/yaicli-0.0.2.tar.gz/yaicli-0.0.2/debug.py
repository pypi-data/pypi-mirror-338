from yaicli import ShellAI


def main():
    ai = ShellAI()
    ai.load_config()
    r = ai.get_command_from_llm("列出当前目录中所有的文件,包含隐藏文件")
    print(r)


if __name__ == "__main__":
    main()
