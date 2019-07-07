class ContentFilter:
    def __init__(self, name):
        openedFile = False
        self.name=name
        while not openedFile:
            try:
                myFile=open(self.name,'r')
            except (FileNotFoundError, TypeError, OSError):
                self.name=input("File name invalid. Try again")
                continue
            else:
                openedFile = True
        self.mylines=myFile.readlines()
        cont=""
        for line in self.mylines:
            cont= cont+line

        self.contents=cont
        myFile.close()

    def uniform(self, out, mode='w', case='upper'):
        if mode not in ['w','a','x']:
            raise ValueError("Choose mode from: 'w', 'x' or 'a'")
        if case not in ['upper','lower']:
            raise ValueError("Choose mode from: 'w', 'x' or 'a'")

        try:
            myOut= open(out,mode)

            if case =='upper':
                for line in self.contents:
                    myOut=write(line.upper())
            elif case=='lower':
                for line in self.contents:
                    myOut=write(line.lower())
        finally:
            myOut.close()
