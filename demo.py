import winrandom, struct
"""
Writes approximately 2,7 KB of data from winrandom to a file. The file can be then
passed into a statistical test engine e.g. FIPS 140-1. Just to make sure the
winrandom module works as expected :)
"""

fout = open('test.rnd', 'wcb')

for i in range(700):
    fout.write(struct.pack('L', winrandom.long()))

fout.close()    
    
