import sys, time
 
# 진도바
class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 60):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self, name):
        progress = self.width * self.count / 1189
        sys.stdout.write('버전"{0}" 크롤링중:{1:4}/1189: '.format(name, self.count))
        sys.stdout.write('#' * int(progress) + '-' * (self.width - int(progress)) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()