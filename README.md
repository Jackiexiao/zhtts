# ZhTTS
[中文](https://github.com/Jackiexiao/zhtts/blob/main/README-zh.md)

A demo of zh/Chinese Text to Speech system run on CPU in real time. (fastspeech2 + mbmelgan)

> RTF(real time factor): 0.2 with cpu: Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz 24khz audio use fastspeech2, RTF1.6 for tacotron2

This repo is **mainly based on** [TensorFlowTTS](https://github.com/TensorSpeech/TensorFlowTTS) with little improvement.

* tflite model come from [colab](https://colab.research.google.com/drive/1Ma3MIcSdLsOxqOKcN1MlElncYMhrOg3J?usp=sharing), thx to [@azraelkuan](https://github.com/azraelkuan)
* add pause at punctuation
* add TN (Text Normalization) from [chinese_text_normalization](https://github.com/speechio/chinese_text_normalization)

## demo wav 
text = "2020年，这是一个开源的端到端中文语音合成系统"

* [fastspeech2 - demo.wav](http://uploader.shimo.im/f/ntu3b9McVNp7yQPb.wav)
* [fastspeech2 - news](http://uploader.shimo.im/f/78vEowrUp3nzVhLX.mp3)
* [tacotron2 - news](http://uploader.shimo.im/f/KTqcpOjna4bJ3Khn.mp3)

## Install 
```
pip install zhtts
```
or clone this repo, then ` pip install . `

## Usage 
```python
import zhtts

text = "2020年，这是一个开源的端到端中文语音合成系统"
tts = zhtts.TTS() # use fastspeech2 by default

tts.text2wav(text, "demo.wav")
>>> Save wav to demo.wav

tts.frontend(text)
>>> ('二零二零年，这是一个开源的端到端中文语音合成系统', 'sil ^ er4 #0 l ing2 #0 ^ er4 #0 l ing2 #0 n ian2 #0 #3 zh e4 #0 sh iii4 #0 ^ i2 #0 g e4 #0 k ai1 #0 ^ van2 #0 d e5 #0 d uan1 #0 d ao4 #0 d uan1 #0 zh ong1 #0 ^ uen2 #0 ^ v3 #0 ^ in1 #0 h e2 #0 ch eng2 #0 x i4 #0 t ong3 sil')

tts.synthesis(text)
>>> array([0., 0., 0., ..., 0., 0., 0.], dtype=float32)
```

### web api demo
clone this repo, `pip install flask` first, then
```
python app.py
```
* visit http://localhost:5000 for tts interaction
* do HTTP GET at http://localhost:5000/api/tts?text=your%20sentence to get WAV audio back:

```sh
$ curl -o "helloworld.wav" "http://localhost:5000/api/tts?text=%E4%BD%A0%E5%A5%BD%E4%B8%96%E7%95%8C"
```
`%E4%BD%A0%E5%A5%BD%E4%B8%96%E7%95%8C` is url code of"你好，世界！"

## Use tacotron2 instead of fastspeech2
wav generate from tacotron model is better than fast speech, however tacotron is much slower , to use Tacotron, change code
```python
import zhtts
tts = zhtts.TTS(text2mel_name="TACOTRON")
# tts = zhtts.TTS(text2mel_name="FASTSPEECH2")
```
