# zhtts
A demo of zh/Chinese Text to Speech system run on CPU in real time.

一个在CPU实时运行的中文语音合成系统Demo。
> 实时率(rtf)  0.2 with cpu: Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz


This repo is mainly based on [TensorFlowTTS](https://github.com/TensorSpeech/TensorFlowTTS) with little improvement.

核心TTS代码和模型来源于：[TensorFlowTTS](https://github.com/TensorSpeech/TensorFlowTTS)，在此基础上，做了一些微小的改进，如：
* 使用tflite，模型来源：https://colab.research.google.com/drive/1Ma3MIcSdLsOxqOKcN1MlElncYMhrOg3J?usp=sharing
* 在标点符号处停顿（加入#3）
* 添加中文正则化（TN Text Normalization）

## demo wav 合成样音
text = "2020年，这是一个开源的端到端中文语音合成系统"

[demo.wav click to play](https://raw.githubusercontent.com/jackiegeek/zhtts/main/demo.wav)
## Install 安装
clone this repo
```shell
pip install "tensorflow>=2.3.0" numpy scipy pypinyin
```
for window , `pip install "tensorflow>=2.4.0rc"` because [this](https://www.tensorflow.org/lite/guide/ops_select#python)

## Usage 使用说明
```python
import zhtts

text = "2020年，这是一个开源的端到端中文语音合成系统"
tts = zhtts.TTS()
tts.text2wav(text, "demo.wav")
```
```python
tts.frontend(text)
>>> ('二零二零年，这是一个开源的端到端中文语音合成系统', 'sil ^ er4 #0 l ing2 #0 ^ er4 #0 l ing2 #0 n ian2 #0 #3 zh e4 #0 sh iii4 #0 ^ i2 #0 g e4 #0 k ai1 #0 ^ van2 #0 d e5 #0 d uan1 #0 d ao4 #0 d uan1 #0 zh ong1 #0 ^ uen2 #0 ^ v3 #0 ^ in1 #0 h e2 #0 ch eng2 #0 x i4 #0 t ong3 sil')

tts.synthesis(text)
>>> array([0., 0., 0., ..., 0., 0., 0.], dtype=float32)
```

### 搭建一个web演示服务
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

## TODO 
- [ ] 使用准确率更高的 g2pM ？
- [ ] 支持合成英文字母
- [ ] 使用tflite_runtime
- [ ] 更高的表现力/自然度
- [ ] 支持流式合成

