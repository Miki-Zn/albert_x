import asyncio
import random
import argparse
from x_client import get_x_client
from llm_agent import analyze_text
from tg_bridge import send_financial_alert, send_alpha_alert, bot
from database import SessionLocal, ProcessedTweet

x_client = get_x_client()
db = SessionLocal()

async def process_mentions(mode: str):
    me = x_client.get_me()
    if not me.data:
        return

    mentions = x_client.get_users_mentions(id=me.data.id)
    if not mentions.data:
        return

    for tweet in mentions.data:
        exists = db.query(ProcessedTweet).filter(ProcessedTweet.tweet_id == str(tweet.id)).first()
        if exists:
            continue

        intent, analysis = await analyze_text(tweet.text)
        
        jitter = random.randint(60, 2700)
        await asyncio.sleep(jitter)

        if intent == "financial":
            action_id = str(random.randint(10000, 99999))
            await send_financial_alert("user", tweet.text, analysis, action_id)
        elif intent == "alpha":
            await send_alpha_alert("@new_gem", analysis)
        else:
            if mode == "evening":
                x_client.create_tweet(text=analysis[:280], in_reply_to_tweet_id=tweet.id)

        new_record = ProcessedTweet(tweet_id=str(tweet.id), intent=intent)
        db.add(new_record)
        db.commit()

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['morning', 'evening'], default='morning')
    args = parser.parse_args()
    
    await process_mentions(args.mode)
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())