# ZhTTS
A demo of zh/Chinese Text to Speech system run on CPU in real time.

> RTF(real time factor): 0.2 with cpu: Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz 24khz use fastspeech2, rtf 1.6 for tacotron2


This repo is mainly based on [TensorFlowTTS](https://github.com/TensorSpeech/TensorFlowTTS) with little improvement.

* tflite model come from [colab](https://colab.research.google.com/drive/1Ma3MIcSdLsOxqOKcN1MlElncYMhrOg3J?usp=sharing)
* add pause at punctuation (use #3)
* add TN (Text Normalization) from [chinese_text_normalization](https://github.com/speechio/chinese_text_normalization)

## demo wav 
text = "2020年，这是一个开源的端到端中文语音合成系统"

* [fastspeech2 - demo.wav](https://gitee.com/jackiegeek/zhtts/raw/master/demo.wav)
* [fastspeech2 - news](https://gitee.com/jackiegeek/zhtts/raw/master/fastspeech2.wav)
* [tacotron2 - news](https://gitee.com/jackiegeek/zhtts/raw/master/tacotron2.wav)

## Install 
clone this repo
```shell
pip install "tensorflow>=2.3.0" numpy scipy pypinyin
```
for window , `pip install "tensorflow>=2.4.0rc"` because [this](https://www.tensorflow.org/lite/guide/ops_select#python)

## Usage 
```python
import zhtts

text = "2020年，这是一个开源的端到端中文语音合成系统"
tts = zhtts.TTS() # use fastspeech2 by default
tts.text2wav(text, "demo.wav")
```
```python
tts.frontend(text)
>>> ('二零二零年，这是一个开源的端到端中文语音合成系统', 'sil ^ er4 #0 l ing2 #0 ^ er4 #0 l ing2 #0 n ian2 #0 #3 zh e4 #0 sh iii4 #0 ^ i2 #0 g e4 #0 k ai1 #0 ^ van2 #0 d e5 #0 d uan1 #0 d ao4 #0 d uan1 #0 zh ong1 #0 ^ uen2 #0 ^ v3 #0 ^ in1 #0 h e2 #0 ch eng2 #0 x i4 #0 t ong3 sil')

tts.synthesis(text)
>>> array([0., 0., 0., ..., 0., 0., 0.], dtype=float32)
```

### web api demo
```
python app.py
```
* visit http://localhost:5000 
* do HTTP GET at http://localhost:5000/api/tts?text=your%20sentence to get WAV audio back:

```sh
$ curl -G --output - \
    --data-urlencode 'text=你好，世界！' \
    'http://localhost:5000/api/tts' | \
    aplay
```

## Use tacotron2 instead of fastspeech2
wav generate from tacotron model is better than fast speech, however tacotron is much slower due to some issue (rtf 1.63 with cpu: Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz 24khz use fastspeech ), to use Tacotron
```python
import zhtts
tts = zhtts.TTS(text2mel_name="TACOTRON")
# tts = zhtts.TTS(text2mel_name="FASTSPEECH2")
```


## TODO 
- [ ] more accurate g2p by using g2pM?
- [ ] support synthesis English alpha 
- [ ] use tflite_runtime without full tensorflow
- [ ] stream tts

