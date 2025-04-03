import json

from aiddit.create.prompts.create_renshe_comprehension_prompt import (
    NOTE_PROMPT,
    HISTORY_NOTE_SUMMARY,
    USER_ACCOUNT_INFO_PROMPT
)
import aiddit.utils as utils
import aiddit.model.google_genai as google_genai


def comprehension_topic_mode(history_note_list, account_user_info):
    history_message = []

    user_account_info_prompt = USER_ACCOUNT_INFO_PROMPT.format(account_name=account_user_info.get("account_name"),
                                    account_description=account_user_info.get("description"),
                                    note_count=len(history_note_list))
    user_account_info_conversation_message = google_genai.GenaiConversationMessage.text_and_images(user_account_info_prompt,
                                                                                               account_user_info.get("avatar_url"))
    history_message.append(user_account_info_conversation_message)

    for index, h_note in enumerate(history_note_list):
        # 历史参考帖子
        h_note_images = utils.remove_duplicates(h_note.get("images"))
        history_note_prompt = NOTE_PROMPT.format(note_index=index + 1,
                                                 channel_content_id=h_note.get("channel_content_id"),
                                                 title=h_note.get("title"), body_text=h_note.get("body_text"),
                                                 image_count=len(h_note_images))
        history_note_conversation_message = google_genai.GenaiConversationMessage.text_and_images(history_note_prompt,
                                                                                                  h_note_images)
        history_message.append(history_note_conversation_message)

    history_note_summary_prompt = HISTORY_NOTE_SUMMARY.format(note_count=len(history_note_list))
    ask_message_conversation = google_genai.GenaiConversationMessage.one("user", history_note_summary_prompt)
    message_response = google_genai.google_genai_output_images_and_text(ask_message_conversation,
                                                                        model=google_genai.MODEL_GEMINI_2_5_PRO_EXPT_0325,
                                                                        history_messages=history_message,
                                                                        response_mime_type="application/json")

    response_content = message_response.content[0].value
    print(response_content)

    return json.loads(response_content)


if __name__ == "__main__":
    renshe_path = "/Users/nieqi/Documents/workspace/python/image_article_comprehension/aigc_data/renshe_comprehension/account_摸鱼阿希_617a100c000000001f03f0b9.json"
    renshe_info = json.load(open(renshe_path, "r"))
    history_note_dir_path = renshe_info.get("history_note_dir_path")
    account_info = renshe_info.get("account_info")
    note_list = utils.load_from_json_dir(history_note_dir_path)
    topic_mode = comprehension_topic_mode(note_list, account_info)
    pass
