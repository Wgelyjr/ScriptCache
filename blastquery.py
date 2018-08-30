import os
import time
import mmap
import random
from collections import defaultdict
#Insert your command here
cmd = r"blastn -task blastn-short -db nt -query C:\Users\Liam\Documents\Research\DSCAM\dockid.fasta -outfmt 6 -out dock.txt -remote"
os.system(cmd)
#This is where it detects the text file
filename = dock.txt #Replace dock.txt with your desired filename
