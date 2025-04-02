import os

from make_shard_common import make_shards_common
from make_datalist4tokendata import do_get_formatted_datalist_for_token_task
from gxl_ai_utils.utils import utils_file

token_path = "/mnt/sfs/asr/code/gxl_ai_utils/eggs/cat_and_dogs_stage2/cosyvoice1_text2token/exp/output/attention_rescoring/0.pt/text_aishell_chat_znlin.scp"
wav_path = "/mnt/sfs/asr/update_data/raw_data/asr_chat_znlin_2025-1-24/wav.scp"
text_path = "/mnt/sfs/asr/update_data/raw_data/asr_chat_znlin_2025-1-24/text.scp"
output_path = "/mnt/sfs/asr/update_data/speech2text_token/asr_chat_znlin_enhance_2025-3-5"
utils_file.makedir_sil(output_path)
dict_list = do_get_formatted_datalist_for_token_task(
    wav_path,
    text_path,
    token_path,
    "speech2text_asr_chat_znlin_enhance_2025-3-5"
)
data_list_path = os.path.join(output_path, "data.list")
utils_file.write_dict_list_to_jsonl(
    dict_list,
    data_list_path
)
shards_dir = os.path.join(output_path, "shards")
utils_file.makedir_sil(shards_dir)
make_shards_common(
    data_list_path,
    shards_dir,
    num_threads=32
)