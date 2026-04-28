# 贡献指南

感谢你愿意参与诸暨话开放语料库。这个项目最重要的原则是：先保护发音人，再整理资料。

## 贡献流程

1. 阅读采集说明  
   请先阅读 `docs/collection-guide.md`、`docs/transcription-guide.md` 和 `docs/ethics-and-privacy.md`。

2. 获取发音人授权  
   录音前必须让发音人理解录音用途、公开范围、是否允许 AI 训练、是否允许商业使用，并记录授权等级。可参考 `docs/consent-template.md`。

3. 按命名规范录音  
   推荐格式为 WAV 或 FLAC。文件名示例：

   ```text
   ZJ001_S001_20260429_free_001.wav
   ```

4. 填写元数据  
   至少填写：

   - `data/speakers.csv`
   - `data/recordings.csv`
   - `data/segments.csv`

   如需生成机器学习用的扁平表，也可填写 `data/metadata.csv`。

5. 转写与释义  
   按三层结构填写：

   - `dialect_text`
   - `mandarin_translation`
   - `normalized_text`

6. 本地校验

   ```bash
   python scripts/validate_metadata.py
   ```

7. 提交 Pull Request  
   请在 PR 中说明资料来源、授权等级、采集地区、是否包含音频、是否包含敏感信息。

8. 维护者审核  
   维护者会检查授权、隐私、命名、字段完整性和转写质量。必要时会请贡献者补充说明。

## 不接受的内容

- 无授权来源的音频或视频。
- 从微信群、短视频平台、新闻视频、家庭群转发材料中直接搬运的内容。
- 公开真实姓名、手机号、身份证、详细住址等敏感信息的材料。
- 嘲笑、贬低、攻击某地口音或发音人的内容。

