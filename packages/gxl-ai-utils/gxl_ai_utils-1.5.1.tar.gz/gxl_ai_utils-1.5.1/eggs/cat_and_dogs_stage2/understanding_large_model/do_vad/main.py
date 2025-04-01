import torch
import torchaudio
import numpy as np


def remove_silence_torchaudio_with_duration(input_path, output_path, threshold=0.01, silence_duration_threshold=0.1):
    # 读取音频文件
    waveform, sr = torchaudio.load(input_path)
    # 计算音频的能量
    energy = torch.sum(waveform ** 2, dim=0)
    # 找到静音部分的索引
    is_silent = energy < threshold
    silent_indices = torch.where(is_silent)[0]
    # 计算静音部分的持续时间
    silent_durations = []
    start = silent_indices[0]
    for i in range(1, len(silent_indices)):
        if silent_indices[i] - silent_indices[i - 1] == 1:
            continue
        end = silent_indices[i - 1]
        duration = (end - start) / sr
        silent_durations.append((start, end, duration))
        start = silent_indices[i]
    # 处理最后一个静音段
    end = silent_indices[-1]
    duration = (end - start) / sr
    silent_durations.append((start, end, duration))
    # 找到需要剪切的静音段的起始和结束索引
    silent_to_cut = [(start, end) for start, end, duration in silent_durations if duration > silence_duration_threshold]
    # 找到非静音段的起始和结束索引
    non_silent_segments = []
    start = 0
    for cut_start, cut_end in silent_to_cut:
        non_silent_segments.append((start, cut_start))
        start = cut_end + 1
    non_silent_segments.append((start, len(waveform[0])))
    # 拼接非静音段
    new_waveform = torch.cat([waveform[:, start:end] for start, end in non_silent_segments], dim=1)
    # 保存新的音频文件
    torchaudio.save(output_path, new_waveform, sr)


import torch
import torchaudio


def remove_silence_torchaudio_ends(input_path, output_path, threshold=0.01, silence_duration_threshold=0.03):
    # 读取音频文件
    waveform, sr = torchaudio.load(input_path)
    # 计算音频的能量
    energy = torch.sum(waveform ** 2, dim=0)
    # 找到静音部分的索引
    is_silent = energy < threshold
    silent_indices = torch.where(is_silent)[0]
    # 计算静音部分的持续时间
    silent_durations = []
    start = silent_indices[0]
    for i in range(1, len(silent_indices)):
        if silent_indices[i] - silent_indices[i - 1] == 1:
            continue
        end = silent_indices[i - 1]
        duration = (end - start) / sr
        silent_durations.append((start, end, duration))
        start = silent_indices[i]
    # 处理最后一个静音段
    end = silent_indices[-1]
    duration = (end - start) / sr
    silent_durations.append((start, end, duration))

    # 只考虑首尾的静音段
    silent_to_cut = []
    if silent_durations:
        first_start, first_end, first_duration = silent_durations[0]
        if first_duration > silence_duration_threshold:
            silent_to_cut.append((first_start, first_end))
        last_start, last_end, last_duration = silent_durations[-1]
        if last_duration > silence_duration_threshold:
            silent_to_cut.append((last_start, last_end))

    # 找到非静音段的起始和结束索引
    non_silent_segments = []
    start = 0
    if silent_to_cut:
        if silent_to_cut[0][0] == silent_durations[0][0]:  # 处理开始处的静音段
            start = silent_to_cut[0][1] + 1
        if silent_to_cut[-1][0] == silent_durations[-1][0]:  # 处理结束处的静音段
            end = silent_to_cut[-1][0]
            non_silent_segments.append((start, end))
        else:
            non_silent_segments.append(start, len(waveform[0]))
    else:  # 如果没有需要剪切的静音段，直接复制整个音频
        non_silent_segments = [(0, len(waveform[0]))]

    # 拼接非静音段
    new_waveform = torch.cat([waveform[:, start:end] for start, end in non_silent_segments], dim=1)
    # 保存新的音频文件
    torchaudio.save(output_path, new_waveform, sr)


# 示例调用
input_audio_path = 'test.wav'
output_audio_path = 'output_audio.wav'
remove_silence_torchaudio_ends(input_audio_path, output_audio_path)