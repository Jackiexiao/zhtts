import os
import numpy as np
from pathlib import Path
import tensorflow as tf 
from scipy.io import wavfile

from .tensorflow_tts.processor import BakerProcessor

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
asset_dir = Path(__file__).parent / "asset"


class TTS():
    def __init__(self, text2mel_name="FASTSPEECH2"):
        """text2mel_name: ["FASTSPEECH2", "TACOTRON"] """
        self.sample_rate = 24000
        self.processor = BakerProcessor(
            data_dir=None, loaded_mapper_path=asset_dir / "baker_mapper.json")
        self.text2mel_name = text2mel_name
        self.acoustic = tf.lite.Interpreter(model_path=str(asset_dir / 'fastspeech2_quan.tflite'))
        self.vocoder = tf.lite.Interpreter(model_path=str(asset_dir / 'mb_melgan.tflite'))

    def prepare_input(self, input_ids):
        input_ids = np.expand_dims(np.array(input_ids, np.int32), 0)
        if self.text2mel_name == "TACOTRON":
            return (input_ids,
                    np.array([input_ids.shape[1]], np.int32),
                    np.array([0], np.int32),)
        elif self.text2mel_name == "FASTSPEECH2":
            return (input_ids,
                    np.array([0], np.int32),
                    np.array([1.0], np.float32),
                    np.array([1.0], np.float32),
                    np.array([1.0], np.float32),)

    def text2mel(self, input_text):
        input_details = self.acoustic.get_input_details()
        output_details = self.acoustic.get_output_details()
        input_ids = self.processor.text_to_sequence(input_text, inference=True)

        self.acoustic.resize_tensor_input(
            input_details[0]['index'], [1, len(input_ids)])
        self.acoustic.allocate_tensors()

        input_data = self.prepare_input(input_ids)
        for i, detail in enumerate(input_details):
            self.acoustic.set_tensor(detail['index'], input_data[i])
        self.acoustic.invoke()

        return self.acoustic.get_tensor(output_details[1]['index'])

    def mel2audio(self, mel):
        input_details = self.vocoder.get_input_details()
        output_details = self.vocoder.get_output_details()
        self.vocoder.resize_tensor_input(input_details[0]['index'], mel.shape)
        self.vocoder.allocate_tensors()
        self.vocoder.set_tensor(input_details[0]['index'], mel)
        self.vocoder.invoke()

        return self.vocoder.get_tensor(output_details[0]['index'])[0, :, 0]

    def synthesis(self, text):
        """ synthesis text to audio

        Args:
            text (str)
        Returns:
            ndarray: audio
        """
        mel = self.text2mel(text)
        audio = self.mel2audio(mel)
        return audio

    def frontend(self, text):
        """ return normalize_text, phoneme_seq for debug

        Args:
            text (str)
        Returns:
            (tuple): tuple containing:

                normalize_text (str):  text after text_normalize
                phoneme (str):  " ".join(phones)
        """
        return self.processor.text_to_phone(text)

    def text2wav(self, text, wavpath):
        """synthesis text and save to wavfile"""
        audio = self.synthesis(text)
        
        wavfile.write(wavpath, self.sample_rate, audio)
        