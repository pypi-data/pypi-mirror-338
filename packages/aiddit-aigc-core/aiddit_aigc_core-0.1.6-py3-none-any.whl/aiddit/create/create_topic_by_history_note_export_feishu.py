import sys

sys.path.append("/Users/nieqi/Documents/workspace/python")
from image_analyzer.utils.feshu import write_data_to_sheet
import pandas as pd
import os
import json
from itertools import groupby

# Directory containing the data files
data_dir = '/Users/nieqi/Documents/workspace/python/image_article_comprehension/aiddit/create/result/topic_result_0401/摸鱼阿希'
data = []

all_result = []
for i in [f for f in os.listdir(data_dir) if f.endswith('.json')]:
    try:
        all_result.append(json.load(open(os.path.join(data_dir, i), 'r')))
    except Exception as e:
        print(f"{i} , {str(e)}")

for result in all_result:
    reference_note = result.get("reference_note", {})
    images = [f"\"{i}\"" for i in reference_note.get('images', [])]

    r = result.get("topic", {})

    if type(r) is list:
        r = r[0]

    topic = r.get("选题结果", {})

    row = {
        '刺激源': f"[{','.join(images)}]",
        '刺激源标题正文': reference_note.get("title", "") + "\n\n" + reference_note.get("body_text", ""),
        "选题": topic.get("选题", ""),
        "选题描述": topic.get("选题描述", ""),
        "选题创作的关键点": json.dumps(topic.get("选题创作的关键点", []), ensure_ascii=False, indent=4),
        "选题产生的逻辑": topic.get("选题产生的逻辑", ""),
    }
    data.append(row)

# Convert DataFrame to list with header
df = pd.DataFrame(data)
header = df.columns.tolist()
data_rows = df.values.tolist()
data_with_header = [header] + data_rows

sheet_token = 'Ty2MsTOSih0B2KtSdAAczl5fnJe'
sheet_id = '5Q8Kck'

write_data_to_sheet(data_with_header, sheet_token=sheet_token,
                    sheetid=sheet_id, )
