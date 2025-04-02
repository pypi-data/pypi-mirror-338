from gxl_ai_utils.utils import utils_file

def do_get_formatted_datalist_for_token_task(input_wav, input_text, input_token, dataset_name):
    """
    这个函是为了给实验室理解大模型任务中要用到的数据生成标准格式的data.list
    标准格式:
      {
  "task": task_tag, # 如 "<TRANSCRIBE>"
  "key":  utt_id, # 如 "IC0001W0007"
  "wav": wav_path, # 如 "/home/backup_nfs/data-ASR/AIShell2/AISHELL-2/iOS/data/wav/C0001/IC0001W0007.wav"
  "txt": text, # 如 "天安门"
  "lang": language, # 如 "<CN>"
  "speaker": speaker_tag, # 如 "spk001"
  "emotion": emotion等分类标签 # 如 "<HAPPY>"
  "gender": 性别标签 # 如 "<MALE>"
  "extra":{class:"label", "duration": wav_length# 单位s，如2.05125，表示2.05秒}
  }

    :param input_text:
    :param input_wav:
    :return:
    """
    if not isinstance(input_wav, dict):
        assert isinstance(input_wav, str)
        input_wav = utils_file.load_dict_from_scp(input_wav)
    if not isinstance(input_text, dict):
        assert isinstance(input_text, str)
        input_text = utils_file.load_dict_from_scp(input_text)
    if not isinstance(input_token, dict):
        assert isinstance(input_token, str)
        input_token = utils_file.load_dict_from_scp(input_token)

    # 对input_token 进行处理
    new_token_dict = {}
    for key, token_str in input_token.items():
        token_list = token_str.strip().split()
        new_token_dict[key] = token_list

    task_tag = "<S2TCHAT> <TEXT2TOKEN>"
    lang = "<CN>"
    speaker = "<NONE>"
    emotion  = "NEUTRAL"
    gender = "<NONE>"
    res_list = []
    for key, wav_path in utils_file.tqdm(input_wav.items(), desc="Generating formatted data.list for ASR task", total=len(input_wav)):
        # txt = input_text[key]  # 别忘了key值的对应性
        if key not in input_text:
            utils_file.logging_warning("Warning: {} not in input_text".format(key))
            continue
        if key not in new_token_dict:
            utils_file.logging_warning("Warning: {} not in input_token".format(key))
            continue
        txt = input_text[key]
        token_list_i = new_token_dict[key]
        duration = 0
        # try:
        #     duration = utils_file.do_get_wav_duration(wav_path)
        # except:
        #     try:
        #         samples, rt = utils_file._get_sample_count_torchaudio(wav_path)
        #         duration = samples / rt
        #     except:
        #         # utils_file.logging_print('Error in getting duration of wav file: {}'.format(wav_path))
        #         duration = 0
        extra = {"duration": duration, "dataset": dataset_name, "speech_token": token_list_i}
        item_dict = {"task": task_tag, "key": key, "wav": wav_path,"txt": txt, "lang": lang, "speaker": speaker, "emotion": emotion, "gender": gender, "extra": extra}
        res_list.append(item_dict)
    return res_list
