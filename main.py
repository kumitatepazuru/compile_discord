import logging
import traceback

from discord.ext import commands

logging.basicConfig(level=logging.INFO,
                    format="\033[38;5;4m%(asctime)s \033[38;5;10m[%(module)s] [%(name)s]=>L%(lineno)d "
                           "\033[38;5;14m[%(levelname)s] \033[0m%(message)s")


class main(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

        # 読み込むコグの名前を格納しておく。
        INITIAL_EXTENSIONS = [
            'cog'
        ]

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # 起動時に動作する処理
    async def on_ready(self):
        # 起動したらターミナルにログイン通知が表示される
        logging.info('Bot logged')


# MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    with open("token") as tk:
        TOKEN = tk.read().splitlines()[0]

    bot = main(command_prefix='*', help_command=None)  # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(TOKEN)  # Botのトークン
