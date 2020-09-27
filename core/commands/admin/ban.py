from core.database.repository.group import GroupRepository
from core import decorators

@decorators.admin.user_admin
def init(update, context):
    chat = update.effective_message.chat_id
    rows = GroupRepository().getById([chat])
    for row in rows:
        print(row['id_group'])
        message = "<b>Id del gruppo:</b> <code>{}</code>\n\n<b>Welcome del gruppo:</b> <code>{}</code>\n\n<b>Regole del gruppo:</b> <code>{}</code>\n\n<b>Lingua del gruppo:</b> <code>{}</code>".format(
            row['id_group'],
            row['welcome_text'],
            row['rules_text'],
            row['languages'])
        context.bot.send_message(chat,message,parse_mode='HTML')