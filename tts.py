import parsesrt,os,pyttsx3, time
from pydub import AudioSegment as adseg, silence
from pydub import effects

srtpath="test1.srt"
sppath="speech1"
threads=[]
parsesrt.parse(srtpath)
# time.sleep(2)
engine = pyttsx3.init()

if not os.path.exists(sppath):
    os.makedirs(sppath)

def ttsx(x):
    engine.save_to_file(parsesrt.lns[x] , os.path.join(sppath,str(x)+".wav"))
    engine.runAndWait()

def getTime(st:str,idx:int)->int:
    a=st.split(" --> ")[idx]
    hh=int(a.split(":")[0])
    mm=int(a.split(":")[1])
    ss=int(a.split(":")[2].replace(",",""))
    # print(hh,mm,ss)
    totalmillisecs=hh*60*60*1000+mm*60*1000+ss
    return totalmillisecs

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def compile():
    nl=len(parsesrt.lns.keys())
    print("Compilation started") 
    holder=adseg.empty()
    lastime=0
    printProgressBar(0, 100, prefix = 'Compiling:', suffix = 'Complete', length = 50)
    newtime=getTime(parsesrt.tsmp[1],0)
    slc=adseg.silent(newtime)
    # lastime=getTime(parsesrt.tsmp[i+1],1)
    holder=holder.append(slc, crossfade=0)
    for i in range(1,nl+1):
        crsfade=0
        # lastime=getTime(parsesrt.tsmp[i+1],1)
        startime=getTime(parsesrt.tsmp[i],0)
        endtime=getTime(parsesrt.tsmp[i],1)
        sublength=endtime-startime
        if not i+1>nl:
            nextime=getTime(parsesrt.tsmp[i+1],0)
        if i==nl:
            nextime=endtime
        midlength=nextime-endtime
        # compensate=midlength*0.25
        part=remove_trailing_silence(adseg.from_file(os.path.join(sppath,str(i)+".wav")))
        # if (len(part) + len(holder))>endtime:
        if len(part) > sublength:
            new_speed=len(part)/(sublength)
            part=part.speedup(new_speed,150,0)
        
        holder=holder.append(part, crossfade=crsfade)
        diff = nextime-len(holder)
        # blanktrack=nextime-endtime
        slc=adseg.silent(diff)
        holder=holder.append(slc, crossfade=crsfade)
        # compensate=(lastime-newtime)-len(part)
        # lastime-=compensate
        printProgressBar(i, nl, prefix = 'Compiling:', suffix = 'Complete', length = 50)

    holder.export("full2.wav", format="wav")
    print("compilation finished")
# # for key in parsesrt.tsmp.keys():
# #     part=adseg.from_file(os.path.join(sppath,str(key)+".wav"))
# #     holder=holder.append(part)

def remove_trailing_silence(sound):
    endtrim=silence.detect_leading_silence(sound.reverse())
    return sound[:len(sound)-endtrim]


print("TTS started")
start_time = time.time()
nl=len(parsesrt.lns.keys())

printProgressBar(0, 100, prefix = 'TTS:', suffix = 'Converted', length = 50)
for key in parsesrt.lns.keys():
    # print(key)
    ttsx(key) #--SKIP FOR TESTING
    printProgressBar(key, nl, prefix = 'TTS:', suffix = 'Converted', length = 50)

print("tts finished")

print("TTS converted in %s seconds " % (time.time() - start_time))

start_time = time.time()

compile()

print("Compiled in %s seconds " % (time.time() - start_time))
