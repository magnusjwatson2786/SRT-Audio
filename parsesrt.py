import time


lns={}
tsmp={}
# path="test3.srt"
def parse(path:str)-> None:
    start_time = time.time()
    with open(path,"rb",buffering=512) as srt:
        srtstr=srt.read()#.decode("utf-8")
        # print(srtstr)
        if b"\n\r\n" in srtstr:
            subsplit=b"\n\r\n"
        elif b"\n\n" in srtstr:
            subsplit=b"\n\n"
        # print(b"Subsplit: "+subsplit)
        for subline in srtstr.split(subsplit):
            part=subline.split(b"\n")
            if len(part)>=3:
                tsmp[int(part[0])]=part[1].decode("utf-8")
                ln=b""
                for x in part[2:]:
                    ln+=b" "
                    ln+=x
                    # ln+b" "
                lns[int(part[0])]=ln.decode("utf-8")
            else:
                print(part)
                print("Bad SRT.")

    print("--- %s seconds ---" % (time.time() - start_time))

# parse(path)