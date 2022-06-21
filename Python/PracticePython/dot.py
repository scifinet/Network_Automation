def dot():
    counter = 1
    while counter <= 100:
        print("." * counter)
        if counter != 100:
            counter += 1
            continue
        else:
            while counter > 1:
                a = "." * counter
                print(a.rjust(200))
                counter -= 1
            while counter <= 100:
                b = "." * counter
                print(b.rjust(200))
                if counter != 100:
                    counter += 1
                    continue
                else:
                    while counter > 1:
                        c = "." * counter
                        print(c)
                        counter -= 1
                break

dot()
