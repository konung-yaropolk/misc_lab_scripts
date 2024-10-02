import classes as c
import settings as s


def main():

    for item in s.TO_DO_LIST:

        try:
            der = c.Derivatives(item[0], **item[1])
            der.process_secuence()
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    main()
