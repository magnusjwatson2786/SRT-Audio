<h1> SRT-Audio </h1>
<p align="center">
<img src="https://img.shields.io/github/repo-size/magnusjwatson2786/SRT-Audio">
<img src="https://img.shields.io/github/last-commit/magnusjwatson2786/SRT-Audio">
<img src="https://img.shields.io/github/license/magnusjwatson2786/SRT-Audio">
</p>

Convert your subtitles into audio tracks for whatever reason you might need.

I will be making a GUI version of this program in future.

## Screenshots
![Alt text](screenshots/img1.png?raw=true "SRT-Audio")

## Dependencies
- [Python]
- [Pyttsx3] (for text-to-speech)
- [Pydub] (for audio manipulation)


## Run
To run this program, clone it to your local machine using: 
```sh
git clone https://github.com/magnusjwatson2786/SRT-Audio.git
```
then cd to the repo directory and hit:.
```sh
python -m pip install -r requirements.txt --user
python tts.py
```
Or just double-click on the start.bat file to run.

Note:  Mac OS X / Linux users may need to run the following before executing the script.
```sh
chmod +x start.sh
```

## Usage

1. Replace the values for `srtpath` and `sppath` variables in the `tts.py` file with the path to your srt file and output audio file respectively.

2. Run as specified above.

Simple as that!

## License

MIT

**Free Software, Hell Yeah!**

*Happy Coding!*

[//]: # (links)
    
   [Python]: <https://www.python.org/>
   [Pyttsx3]: <https://pypi.org/project/pyttsx3/>
   [Pydub]: <https://github.com/jiaaro/pydub>
   
