# 元数据字段说明

本项目使用多个 CSV 文件保存元数据。所有字段都应尽量填写；不确定或不适用时可使用空值，但不要编造真实个人信息。

## speakers.csv

- `speaker_id`：发音人匿名编号，例如 `S001`。
- `birth_year`：出生年份，可为空或使用大致年份。
- `age_group`：年龄组，例如 `60s`、`70s`、`80s`、`90s`。
- `gender_optional`：性别，可选填。
- `birth_place`：出生地，可写到乡镇或更粗粒度。
- `township`：诸暨地区分类，例如 `暨阳/城区`、`枫桥`。
- `years_in_zhuji`：在诸暨生活年数。
- `home_language`：家庭常用语言或方言。
- `self_dialect_level`：自评诸暨话熟练度，例如 `native`、`fluent`、`partial`。
- `consent_level`：授权等级，`A`、`B` 或 `C`。
- `notes`：其他说明，不要写敏感信息。

## recordings.csv

- `recording_id`：录音编号，例如 `ZJ001_S001_20260429_free_001`。
- `speaker_id`：对应发音人编号。
- `date`：录音日期，格式为 YYYY-MM-DD。
- `location_type`：录音地点类型，例如 `home`、`outdoor`、`office`。
- `device`：录音设备，例如手机型号或录音笔。
- `format`：文件格式，例如 `wav`、`flac`、`m4a`。
- `duration_sec`：录音总时长，单位秒。
- `genre`：录音类型，例如 `wordlist`、`sentence`、`free`、`conversation`、`story`。
- `consent_level`：本录音适用授权等级。
- `license`：许可说明，例如 `CC BY-NC 4.0` 或 `speaker consent only`。
- `notes`：环境、噪声、采集情况等。

## segments.csv

- `segment_id`：片段编号，例如 `ZJ001_S001_0001`。
- `recording_id`：所属录音编号。
- `start_sec`：片段开始时间，单位秒。
- `end_sec`：片段结束时间，单位秒。
- `speaker_id`：说话人编号。
- `dialect_text`：诸暨话转写。
- `mandarin_translation`：普通话释义。
- `normalized_text`：规范化文本。
- `topic`：主题，例如 `天气`、`买菜`、`年俗`。
- `quality`：音频质量，例如 `good`、`fair`、`noisy`。
- `review_status`：审核状态，例如 `draft`、`reviewed`。

## metadata.csv

`metadata.csv` 是面向训练、检索或发布的扁平化索引表。

- `segment_id`：片段编号。
- `audio_path`：对应音频片段路径。
- `dialect_text`：诸暨话转写。
- `mandarin_translation`：普通话释义。
- `speaker_id`：发音人编号。
- `township`：地区分类。
- `age_group`：年龄组。
- `gender_optional`：性别，可选填。
- `topic`：主题。
- `license`：许可说明。

