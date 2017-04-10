
l = [5555,1,54,55555,25,466656,8777,1]


class Demo(object):

    def sorting(self, l):
        for i in range(0, len(l)):
            for j in range(i+1, len(l)):
                if l[i] <= l[j]:
                 pass
                else:
                    l[i], l[j] = l[j], l[i]
        return l

    def fibonacci(self, n):

        a,b = 0,1
        l = []
        l.extend([a,b])
        for i in range(n):
            c = a + b
            l.append(c)
            a, b = b, c
        return l

if __name__ == '__main__':
    a = Demo()
    a.fibonacci(1)
