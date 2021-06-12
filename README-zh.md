# ZhTTS
[English](https://github.com/Jackiexiao/zhtts/blob/main/README.md)

在CPU上实时运行的中文语音合成系统（一个简单的示例，使用 Fastspeech2 + MbMelGan），但总体效果离“能用”还有很大差距，供大家参考

> 实时率RTF：0.2 Cpu: Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz 采样率24khz  fastspeech2, RTF1.6 for tacotron2

这个项目**主要依赖**于 [TensorFlowTTS](https://github.com/TensorSpeech/TensorFlowTTS)，做了非常简单的改进：

* tflite 模型来源于[colab](https://colab.research.google.com/drive/1Ma3MIcSdLsOxqOKcN1MlElncYMhrOg3J?usp=sharing), 感谢[@azraelkuan](https://github.com/azraelkuan)
* 在标点符号处停顿
* 增加了简单的文本正则化（数字转汉字）TN (Text Normalization) 使用 [chinese_text_normalization](https://github.com/speechio/chinese_text_normalization)

## 合成效果
text = "2020年，这是一个开源的端到端中文语音合成系统"

* [zhtts synthesis mp3](https://shimo.im/docs/tcXPY9pdrdRdwqk6/ )


## 安装
```
pip install zhtts
```
or clone this repo, then ` pip install . `

## 使用
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

### 网页 api demo
下载这个项目, `pip install flask` first, then
```
python app.py
```
* 访问 http://localhost:5000 可以直接进行语音合成交互
* do HTTP GET at http://localhost:5000/api/tts?text=your%20sentence to get WAV audio back:

```sh
$ curl -o "helloworld.wav" "http://localhost:5000/api/tts?text=%E4%BD%A0%E5%A5%BD%E4%B8%96%E7%95%8C"
```
`%E4%BD%A0%E5%A5%BD%E4%B8%96%E7%95%8C` 是"你好，世界！"的 url 编码

## 使用 Tacotron2 模型
某些情况下 Tacotron2 合成效果会好一点，不过合成速度会慢不少
```python
import zhtts
tts = zhtts.TTS(text2mel_name="TACOTRON")
# tts = zhtts.TTS(text2mel_name="FASTSPEECH2")
```
