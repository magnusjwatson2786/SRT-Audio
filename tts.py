import parsesrt,os,pyttsx3,time
from pydub import AudioSegment as adseg

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
    # print(totalsecs)
    return totalmillisecs

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

print("TTS started")
start_time = time.time()
nl=len(parsesrt.lns.keys())

printProgressBar(0, 100, prefix = 'TTS:', suffix = 'Converted', length = 50)
for key in parsesrt.lns.keys():
    # print(key)
    ttsx(key)
    printProgressBar(key, nl, prefix = 'TTS:', suffix = 'Converted', length = 50)


print("tts finished")

def compile():
    print("Compilation started") 
    holder=adseg.empty()
    lastime=0
    printProgressBar(0, 100, prefix = 'Compiling:', suffix = 'Complete', length = 50)
    for i in range(nl):
        # print(i+1)
        newtime=getTime(parsesrt.tsmp[i+1],0)
        slc=adseg.silent(newtime-lastime)
        lastime=getTime(parsesrt.tsmp[i+1],1)
        holder=holder.append(slc, crossfade=0)
        part=adseg.from_file(os.path.join(sppath,str(i+1)+".wav"))
        compensate=(lastime-newtime)-len(part)
        holder=holder.append(part, crossfade=0)
        lastime-=compensate
        printProgressBar(i+1, nl, prefix = 'Compiling:', suffix = 'Complete', length = 50)

    holder.export("full.wav", format="wav")
    print("compilation finished")

print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()

compile()

print("--- %s seconds ---" % (time.time() - start_time))


