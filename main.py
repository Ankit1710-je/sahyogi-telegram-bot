import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from drive_utils import upload_file_to_drive
from config import TELEGRAM_BOT_TOKEN, CLASSIFICATION_KEYWORDS
from classifier_llm import classify_file

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.document:
        return

    document = update.message.document
    file_name = document.file_name

    logger.info(f"Received file: {file_name}")

    # Download the file from Telegram
    new_file = await context.bot.get_file(document.file_id)
    file_path = f"/tmp/{file_name}"
    await new_file.download_to_drive(file_path)

    logger.info(f"Downloaded file to: {file_path}")

    # Classify the file
    category = classify_file(file_name, CLASSIFICATION_KEYWORDS)
    logger.info(f"Classified as: {category}")

    # Upload to Google Drive
    drive_file_url = upload_file_to_drive(file_path, file_name, category)

    # Reply to user
    await update.message.reply_text(
        f"✅ File received and uploaded.\n\n📁 Category: *{category}*\n📂 [Open in Drive]({drive_file_url})",
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))

    logger.info("🤖 Sahyogi LLM Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
<PLACEHOLDER: Will add once re-uploaded>