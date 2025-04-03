import json
import os
from prompts.create_topic_by_history_note_prompt import (
    CREATE_TOPIC_BY_HISTORY_NOTE_PROMPT,
    NOTE_PROMPT,
)
import aiddit.utils as utils
import aiddit.model.google_genai as google_genai


def create_topic_from_history_note(stimulus_note, history_note_list):
    history_message = []
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

    stimulus_note_images = utils.remove_duplicates(stimulus_note.get("images"))
    create_topic_by_history_note_prompt = CREATE_TOPIC_BY_HISTORY_NOTE_PROMPT.format(note_count=len(history_note_list),
                                                                                     channel_content_id=stimulus_note.get(
                                                                                         "channel_content_id"),
                                                                                     title=stimulus_note.get("title"),
                                                                                     body_text=stimulus_note.get(
                                                                                         "body_text"),
                                                                                     image_count=len(
                                                                                         stimulus_note_images))
    ask_message_conversation = google_genai.GenaiConversationMessage.text_and_images(
        create_topic_by_history_note_prompt, stimulus_note_images)
    ask_response_conversation = google_genai.google_genai_output_images_and_text(ask_message_conversation,
                                                                                 model=google_genai.MODEL_GEMINI_2_5_PRO_EXPT_0325,
                                                                                 history_messages=history_message,
                                                                                 response_mime_type="application/json")

    print(ask_response_conversation.content[0].value)

    return json.loads(ask_response_conversation.content[0].value)


if __name__ == "__main__":
    history_note_dir_path = "/Users/nieqi/Documents/workspace/python/image_article_comprehension/aigc_data/note_data/account_摸鱼阿希_617a100c000000001f03f0b9"

    hnl = utils.load_from_json_dir(history_note_dir_path)

    stimulus_note_dir = "/Users/nieqi/Documents/workspace/python/image_article_comprehension/aiddit/xhs/search_result/搞笑 生活 职场"

    save_output_dir = "/Users/nieqi/Documents/workspace/python/image_article_comprehension/aiddit/create/result/topic_result_0401/" + \
                      os.path.basename(history_note_dir_path).split("_")[1]

    stimulus_note_list = utils.load_from_json_dir(stimulus_note_dir)

    for stimulus in stimulus_note_list:
        topic_save_path = os.path.join(save_output_dir, stimulus.get("channel_content_id") + ".json")

        if os.path.exists(topic_save_path):
            continue

        topic_result = create_topic_from_history_note(stimulus, hnl)
        result = {
            "reference_note": stimulus,
            "topic": topic_result,
        }
        utils.save(result, topic_save_path)
