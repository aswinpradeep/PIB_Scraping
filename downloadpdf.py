import glob
import pdfkit

txtfiles = [f for f in glob.glob("*.txt")]


pdffiles = []
for txtfilename in txtfiles:
    pdffiles.append(txtfilename.replace(".txt",".pdf"))

downpdffiles = [f for f in glob.glob("*.pdf")]


for filename in pdffiles:
    if filename not in downpdffiles:
        try:
            print("working on",filename)
            url="https://www.pib.gov.in/PressReleasePage.aspx?PRID="+str(filename).replace(".pdf","")
            pdfkit.from_url(url, filename)
            print(filename," downloaded")
        except Exception as e:
            print(e)
            print(filename," *** failed ***")
            file2 = open("pdffailedfiles.txt","a")
            file2.write("\n")
            file2.write(str(filename).replace(".pdf","")) 
            file2.close()




